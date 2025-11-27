"""
Klass för att analysera hälsostudiedata
"""

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

from .statistics import basic_descriptive_stats
from .visualization import plot_bp_histogram, plot_weight_box_by_sex


@dataclass
class HealthAnalyzer:
    """
    Kapslaa analys av hälsostudiedata

    Attributes
    ----------
    df : pd.DataFrame
        DataFrame med hälsodata.
    """

    df: pd.DataFrame

    def describe_basic(self) -> pd.DataFrame:
        """
        Beräkna grundlägggande beskrivande statistik

        Returns
        -------
        pd.DataFrame
            Tabell med medel, median, min och max.
        """
        return basic_descriptive_stats(self.df)

    def show_bp_histogram(self) -> None:
        """
        Visa histogram över systolistisk blodtryck
        """
        plot_bp_histogram(self.df)

    def show_weight_box_by_sex(self) -> None:
        """
        Visa boxplot över vikt per kön
        """
        plot_weight_box_by_sex(self.df)

    def fit_bp_regression(self) -> dict:
        """
        Anpassa en linjär regression för systolisk blodtryck

        Returns
        -------
        dict
            Innehåller koficienter, intercept och R^2
        """
        X = self.df[["age", "weight"]].values
        y = self.df["systolic_bp"].values

        model = LinearRegression()
        model.fit(X, y)

        r2 = model.score(X, y)

        results = {
            "model": model,
            "coefficients": pd.Series(model.coef_, index=["age", "weight"]),
            "intercept": model.intercept_,
            "r2": r2,
        }
        return results
