"""
normalize_keys.py

Responsável por normalizar e enriquecer as chaves categóricas do dataset
principal (dengue, zika, chikungunya) utilizando tabelas auxiliares oficiais.

Tabelas auxiliares utilizadas:
- Agravos (CID → nome do agravo)
- UF
- Distritos
- Bairros

Este módulo NÃO filtra municípios.
Ele apenas normaliza e padroniza informações.
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

def load_agravos() -> pd.DataFrame:
    """
    Carrega a tabela de agravos (CID ↔ nome do agravo).
    """
    return pd.read_csv(
        AUX_PATH / "tabela-dos-agravos.csv",
        sep=";",
        encoding="latin1"
    )


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
    Carrega a tabela de distritos.
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

def normalize_agravo(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza o agravo a partir do código CID.
    """
    agravos = load_agravos()

    agravos = agravos.rename(
        columns={
            "Código CID": "co_cid",
            "Agravo": "agravo_descricao"
        }
    )

    df = df.merge(
        agravos,
        how="left",
        on="co_cid"
    )

    return df


def normalize_uf(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza UF a partir do código da UF.
    """
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
    Aplica todas as normalizações de chaves no DataFrame.

    Ordem:
    1. Agravos
    2. UF
    3. Distritos / Municípios
    4. Bairros
    """

    df = normalize_agravo(df)
    df = normalize_uf(df)
    df = normalize_distrito(df)
    df = normalize_bairro(df)

    return df
