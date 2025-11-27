"""
Visualiseringsfunktion för hälsostudien
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


def plot_bp_histogram(df: pd.DataFrame) -> None:
    """
    Rita histogram över systolistisk blodtryck

    Parameterrs
    ----------
    df : pd.DataFrame
        DataFrame med hälsodata.
    """
    plt.figure()
    plt.hist(df["systolic_bp"], bins=20)
    plt.xlabel("Systoliskt blodtryck (mmHg)")
    plt.ylabel("Antal personer")
    plt.title("Histogram över systoliskt blodtryck")
    plt.show()


def plot_weight_box_by_sex(df: pd.DataFrame) -> None:
    """
    Rita boxplot över vikt per köön

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame med hälsodata.
    """
    plt.figure()
    sns.boxplot(x="sex", y="weight", data=df)
    plt.xlabel("Kön")
    plt.ylabel("Vikt (kg)")
    plt.title("Boxplot över vikt per kön")
    plt.show()
