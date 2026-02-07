import pandas as pd
import numpy as np
from datetime import datetime

def standardize_common_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Padroniza tipos de dados comuns a todos os agravos.
    Espera colunas já selecionadas e renomeadas.
    """

    df = df.copy()

    # -----------------------------
    # Datas
    # -----------------------------
    date_columns = [
        "dt_notificacao",
        "dt_nascimento"
    ]

    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # -----------------------------
    # Sexo
    # -----------------------------
    if "tp_sexo" in df.columns:
        df["tp_sexo"] = (
            df["tp_sexo"]
            .replace({
                "M": "Masculino",
                "F": "Feminino",
                "I": "Ignorado",
                "": np.nan
            })
        )

    # -----------------------------
    # Gestante
    # -----------------------------
    if "tp_gestante" in df.columns:
        df["tp_gestante"] = (
            df["tp_gestante"]
            .replace({
                1: "1º trimestre",
                2: "2º trimestre",
                3: "3º trimestre",
                4: "Idade gestacional ignorada",
                5: "Não gestante",
                9: "Ignorado"
            })
        )

    # -----------------------------
    # Sintomas (0/1)
    # -----------------------------
    symptom_columns = [
        "febre",
        "mialgia",
        "cefaleia",
        "exantema",
        "vomito",
        "nausea",
        "dor_costas",
        "conjuntivite",
        "artrite",
        "artralgia"
    ]

    for col in symptom_columns:
        if col in df.columns:
            df[col] = (
                df[col]
                .replace({1: 1, 2: 0, 9: np.nan})
                .astype("Int64")
            )

    # -----------------------------
    # Idade derivada
    # -----------------------------
    if {"dt_notificacao", "dt_nascimento"}.issubset(df.columns):
        df["idade"] = (
            (df["dt_notificacao"] - df["dt_nascimento"])
            .dt.days // 365
        )

    return df
