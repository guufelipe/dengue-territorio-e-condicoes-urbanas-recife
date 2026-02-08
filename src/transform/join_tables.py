from pathlib import Path
import pandas as pd


# Caminho base do projeto
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_RAW_PATH = PROJECT_ROOT / "data" / "raw"


def _infer_year_from_filename(filename: str) -> int | None:
    """
    Extrai o ano do nome do arquivo (ex: 2020, 2021, ...).
    Retorna None se não encontrar.
    """
    for year in range(2015, 2030):
        if str(year) in filename:
            return year
    return None


def join_agravo_years(
    agravo: str,
    sep: str = ";",
    encoding: str = "latin1"
) -> pd.DataFrame:
    """
    Junta todos os arquivos CSV de um agravo (dengue, zika, chikungunya)
    em um único DataFrame.

    Parâmetros
    ----------
    agravo : str
        Nome do agravo (ex: 'dengue', 'zika', 'chikungunya')
    sep : str
        Separador do CSV
    encoding : str
        Encoding dos arquivos

    Retorno
    -------
    pd.DataFrame
        DataFrame consolidado com todos os anos
    """

    agravo_path = DATA_RAW_PATH / agravo

    if not agravo_path.exists():
        raise FileNotFoundError(f"Pasta não encontrada: {agravo_path}")

    dfs = []

    for csv_file in sorted(agravo_path.glob("*.csv")):
        try:
            df = pd.read_csv(
                csv_file,
                sep=sep,
                encoding=encoding,
                low_memory=False
            )

            # Metadados de rastreabilidade
            df["agravo"] = agravo
            df["ano_origem"] = _infer_year_from_filename(csv_file.name)
            df["arquivo_origem"] = csv_file.name

            dfs.append(df)

        except Exception as e:
            print(f"Erro ao ler {csv_file.name}: {e}")

    if not dfs:
        raise ValueError(f"Nenhum CSV válido encontrado para {agravo}")

    return pd.concat(dfs, ignore_index=True)
