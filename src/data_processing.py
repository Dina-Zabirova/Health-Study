from pathlib import Path
import pandas as pd


def load_data():
    """
    Läser in hälsostudiens CSV-fil och returnerar en DataFrame.
    """
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "health_study_dataset.csv"

    return pd.read_csv(file_path)
