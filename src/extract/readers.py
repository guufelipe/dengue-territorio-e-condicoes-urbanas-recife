import pandas as pd
import json

def read_csv_br(path):
    """
    Leitor padrão para CSVs de dados públicos brasileiros
    """
    return pd.read_csv(
        path,
        sep=";",
        encoding="latin1",
        low_memory=False,
        on_bad_lines="skip"
    )

def read_json(path):
    """
    Leitura padrão de arquivos JSON
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
