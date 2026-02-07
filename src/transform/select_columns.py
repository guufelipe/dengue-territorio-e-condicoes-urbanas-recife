from typing import Dict
import pandas as pd


# =========================================================
# MAPEAMENTO PADRÃO DE COLUNAS (SINAN → PROJETO)
# =========================================================

AGRAVOS_COLUMNS_MAP: Dict[str, str] = {
    # -------------------------
    # Notificação
    # -------------------------
    "NU_NOTIFIC": "num_notificacao",
    "DT_NOTIFIC": "dt_notificacao",
    "ID_MUNICIP": "co_municipio_notificacao",
    "ID_UNIDADE": "co_unidade_notificacao",

    # -------------------------
    # Paciente
    # -------------------------
    "DT_NASC": "dt_nascimento",
    "CS_SEXO": "sexo",
    "CS_GESTANT": "gestante",
    "CS_RACA": "raca_cor",
    "TP_ZONA": "zona_residencia",
    "NM_BAIRRO": "bairro_residencia",

    # -------------------------
    # Clínicos
    # -------------------------
    "FEBRE": "febre",
    "MIALGIA": "mialgia",
    "CEFALEIA": "cefaleia",
    "EXANTEMA": "exantema",
    "VOMITO": "vomito",
    "NAUSEA": "nausea",
    "DOR_COSTAS": "dor_costas",
    "CONJUNTVIT": "conjuntivite",
    "ARTRITE": "artrite",
    "ARTRALGIA": "artralgia",

    # -------------------------
    # Classificação e evolução
    # -------------------------
    "CLASSI_FIN": "classificacao_final",
    "HOSPITAL": "ocorreu_hospitalizacao",
    "EVOLUCAO": "evolucao_caso",
}


# =========================================================
# FUNÇÃO BASE (REUTILIZÁVEL)
# =========================================================

def _selecionar_e_renomear(
    df: pd.DataFrame,
    columns_map: Dict[str, str]
) -> pd.DataFrame:
    """
    Seleciona apenas as colunas existentes no DataFrame
    e renomeia para o padrão do projeto.
    """

    colunas_existentes = [
        col for col in columns_map.keys()
        if col in df.columns
    ]

    df_filtrado = df[colunas_existentes].copy()

    df_filtrado = df_filtrado.rename(
        columns=columns_map
    )

    return df_filtrado


# =========================================================
# FUNÇÕES POR AGRAVO
# =========================================================

def tratar_dados_dengue(df: pd.DataFrame) -> pd.DataFrame:
    """
    Seleção e padronização das colunas de Dengue.
    """
    return _selecionar_e_renomear(df, AGRAVOS_COLUMNS_MAP)


def tratar_dados_zika(df: pd.DataFrame) -> pd.DataFrame:
    """
    Seleção e padronização das colunas de Zika.
    """
    return _selecionar_e_renomear(df, AGRAVOS_COLUMNS_MAP)


def tratar_dados_chikungunya(df: pd.DataFrame) -> pd.DataFrame:
    """
    Seleção e padronização das colunas de Chikungunya.
    """
    return _selecionar_e_renomear(df, AGRAVOS_COLUMNS_MAP)
