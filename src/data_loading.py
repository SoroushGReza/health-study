"""
Funktionner för att läsa in hälsostudiedata.
"""

import pandas as pd


def load_health_data(path: str = "../data/health_study_dataset.csv") -> pd.DataFrame:
    """
    Läs in hälsostudiedatat från CSV  filen

    Parameterrs
    ----------
    path : str
        Sökväg till CSV-filen. Default är relativt projektrooten

    Returns
    -------
    pd.DataFrame
        DataFrame med hälsostudiedata
    """
    df = pd.read_csv(path)
    return df
