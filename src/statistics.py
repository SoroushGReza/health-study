"""
Statistiska beräkningar för hälsostudien
"""

import pandas as pd


def basic_descriptive_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Beräkna medel, median, min och max för centrala variabbler

    Parameterar
    ----------
    df : pd.DataFrame
        DataFrame med hälsodata

    Returns
    -------
    pd.DataFrame
        Tabell med beskrivande statistik
    """
    cols = ["age", "weight", "height", "systolic_bp", "cholesterol"]
    stats = df[cols].agg(["mean", "median", "min", "max"])
    return stats
