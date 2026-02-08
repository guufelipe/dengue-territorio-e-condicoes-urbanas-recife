"""
validate_schema.py

Valida se o DataFrame final atende ao schema mínimo esperado
após as transformações (select, normalize, standardize).

Pode operar em modo estrito (quebra pipeline)
ou permissivo (apenas warnings).
"""

from typing import List, Dict
import pandas as pd


# =====================================================
# Schema esperado
# =====================================================

REQUIRED_COLUMNS: List[str] = [
    # Identificação
    "num_notificacao",
    "agravo",
    "ano_origem",

    # Datas
    "dt_notificacao",
    "dt_nascimento",

    # Paciente
    "tp_sexo",
    "tp_gestante",
    "tp_raca_cor",
    "tp_zona_residencia",

    # Localização
    "co_municipio_residencia",
    "nome_municipio",
    "co_bairro_residencia",
    "bairro_padronizado",

    # Sintomas
    "febre",
    "mialgia",
    "cefaleia",
    "exantema",
    "vomito",
    "nausea",
    "dor_costas",
    "conjuntivite",
    "artrite",
    "artralgia",

    # Evolução
    "tp_classificacao_final",
    "st_ocorreu_hospitalizacao",
    "tp_evolucao_caso"
]


EXPECTED_DTYPES: Dict[str, str] = {
    "num_notificacao": "int",
    "ano_origem": "int",

    "dt_notificacao": "datetime",
    "dt_nascimento": "datetime",

    "febre": "bool_or_int",
    "mialgia": "bool_or_int",
    "cefaleia": "bool_or_int",
    "exantema": "bool_or_int",
}


# =====================================================
# Funções de validação
# =====================================================

def _check_required_columns(df: pd.DataFrame) -> List[str]:
    """
    Retorna lista de colunas ausentes.
    """
    return [col for col in REQUIRED_COLUMNS if col not in df.columns]


def _check_dtypes(df: pd.DataFrame) -> Dict[str, str]:
    """
    Verifica tipos esperados (de forma flexível).
    """
    problems = {}

    for col, expected in EXPECTED_DTYPES.items():
        if col not in df.columns:
            continue

        if expected == "datetime":
            if not pd.api.types.is_datetime64_any_dtype(df[col]):
                problems[col] = "esperado datetime"
        elif expected == "int":
            if not pd.api.types.is_integer_dtype(df[col]):
                problems[col] = "esperado inteiro"
        elif expected == "bool_or_int":
            if not (
                pd.api.types.is_bool_dtype(df[col]) or
                pd.api.types.is_integer_dtype(df[col])
            ):
                problems[col] = "esperado bool ou int"

    return problems


def _null_report(df: pd.DataFrame) -> pd.Series:
    """
    Retorna percentual de nulos por coluna.
    """
    return (df.isna().mean() * 100).round(2)


# =====================================================
# Função principal
# =====================================================

def validate_schema(
    df: pd.DataFrame,
    strict: bool = False,
    verbose: bool = True
) -> bool:
    """
    Valida o DataFrame contra o schema esperado.

    strict=True  → levanta exceção
    strict=False → apenas warnings
    """

    errors = False

    # 1. Colunas obrigatórias
    missing_cols = _check_required_columns(df)
    if missing_cols:
        errors = True
        if verbose:
            print("❌ Colunas obrigatórias ausentes:")
            for col in missing_cols:
                print(f"  - {col}")

    # 2. Tipos
    dtype_issues = _check_dtypes(df)
    if dtype_issues:
        errors = True
        if verbose:
            print("\n⚠️ Problemas de tipo:")
            for col, msg in dtype_issues.items():
                print(f"  - {col}: {msg}")

    # 3. Relatório de nulos (informativo)
    if verbose:
        print("\n📊 Percentual de valores nulos (top 10):")
        print(_null_report(df).sort_values(ascending=False).head(10))

    # 4. Resultado final
    if errors and strict:
        raise ValueError("Schema inválido. Veja mensagens acima.")

    if verbose:
        if errors:
            print("\n⚠️ Schema inválido (modo permissivo)")
        else:
            print("\n✅ Schema validado com sucesso")

    return not errors


# Teste no Notebook: 
# from src.transform.validate_schema import validate_schema
# validate_schema(df_dengue_sel, strict=False)

# No pipeline:
# from src.transform.validate_schema import validate_schema
# validate_schema(df_final, strict=True)