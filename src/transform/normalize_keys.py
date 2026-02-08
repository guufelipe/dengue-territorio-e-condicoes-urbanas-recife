"""
normalize_keys.py

Responsável por normalizar e enriquecer chaves territoriais e categóricas
do dataset principal (dengue, zika, chikungunya) utilizando tabelas
auxiliares oficiais do Recife.

Tabelas auxiliares utilizadas:
- UF
- Distritos
- Bairros

Este módulo:
- NÃO filtra municípios
- NÃO cria recortes analíticos
- APENAS normaliza e enriquece chaves existentes
"""

from pathlib import Path
import pandas as pd


# =====================================================
# Caminhos do projeto
# =====================================================

# src/transform/normalize_keys.py → sobe até a raiz do projeto
PROJECT_ROOT = Path(__file__).resolve().parents[2]

AUX_PATH = PROJECT_ROOT / "data" / "raw" / "tabelas_auxiliares"


# =====================================================
# Loaders das tabelas auxiliares
# =====================================================

def load_uf() -> pd.DataFrame:
    """
    Carrega a tabela de UF.
    """
    return pd.read_csv(
        AUX_PATH / "tabela-uf.csv",
        sep=";",
        encoding="latin1"
    )


def load_distritos() -> pd.DataFrame:
    """
    Carrega a tabela de distritos e municípios.
    """
    return pd.read_csv(
        AUX_PATH / "tabela-distrito.csv",
        sep=";",
        encoding="latin1"
    )


def load_bairros() -> pd.DataFrame:
    """
    Carrega a tabela de bairros.
    """
    return pd.read_csv(
        AUX_PATH / "tabela-de-bairros.csv",
        sep=";",
        encoding="latin1"
    )


# =====================================================
# Normalizações
# =====================================================

def normalize_uf(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza UF a partir do código da UF.
    Executa apenas se a coluna existir no DataFrame.
    """
    if "co_uf_notificacao" not in df.columns:
        return df

    uf = load_uf()

    uf = uf.rename(
        columns={
            "codigo": "co_uf_notificacao",
            "sigla": "uf_sigla",
            "descricao": "uf_nome"
        }
    )

    df = df.merge(
        uf,
        how="left",
        on="co_uf_notificacao"
    )

    return df



def normalize_distrito(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza distritos e municípios.
    """
    required_cols = {"co_distrito_residencia", "co_municipio_residencia"}
    if not required_cols.issubset(df.columns):
        return df

    distritos = load_distritos()

    distritos = distritos.rename(
        columns={
            "Código Distrito": "co_distrito_residencia",
            "Distrito": "nome_distrito",
            "Código Município": "co_municipio_residencia",
            "Nome Município": "nome_municipio"
        }
    )

    df = df.merge(
        distritos,
        how="left",
        on=["co_distrito_residencia", "co_municipio_residencia"]
    )

    return df



def normalize_bairro(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza bairros mantendo o nome original e o nome padronizado.
    """
    if "co_bairro_residencia" not in df.columns:
        return df

    bairros = load_bairros()

    bairros = bairros.rename(
        columns={
            "Nº Localidade": "co_bairro_residencia",
            "Nome Localidade": "bairro_padronizado",
            "Nome Município": "nome_municipio_bairro"
        }
    )

    df = df.merge(
        bairros,
        how="left",
        on="co_bairro_residencia"
    )

    return df



# =====================================================
# Função orquestradora
# =====================================================

def normalize_keys(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica todas as normalizações de chaves territoriais no DataFrame.

    Ordem:
    1. UF
    2. Distritos / Municípios
    3. Bairros
    """

    df = normalize_uf(df)
    df = normalize_distrito(df)
    df = normalize_bairro(df)

    return df
