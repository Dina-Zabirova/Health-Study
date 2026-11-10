import pandas as pd

def calculate_descriptive_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Beräknar medelvärde, median, minimum och maximum
    för utvalda numeriska variabler.
    """
    columns = [                                                     # Väljer kolumnerna som ska analyseras
        "age",
        "weight",
        "height",
        "systolic_bp",
        "cholesterol"
    ]
    stats = df[columns].describe().loc[                             # Beräknar statistiken och väljer de mått som behövs
        ["mean", "50%", "min", "max"]
    ]
    stats = stats.rename(index={"50%": "median"})                   # Byter namn från 50% till median för tydlighetens skull

    return stats.T


def display_descriptive_stats(stats: pd.DataFrame) -> None:
    """
    Skriver ut beskrivande statistik med tydliga namn och enheter.
    """

    labels = {                                                       # Anger tydliga namn och enheter för variablerna
        "age": ("Ålder", "år"),
        "weight": ("Vikt", "kg"),
        "height": ("Längd", "cm"),
        "systolic_bp": ("Systoliskt blodtryck", "mmHg"),
        "cholesterol": ("Kolesterolnivå", "")
    }

    for column, (name, unit) in labels.items():                      # Skriver ut statistiken för varje variabel
        print(f"\n{name} ({unit})" if unit else f"\n{name}")
        print("-" * 30)
        print(f"Medelvärde: {stats.loc[column, 'mean']:.2f}")
        print(f"Median:     {stats.loc[column, 'median']:.2f}")
        print(f"Minimum:    {stats.loc[column, 'min']:.2f}")
        print(f"Maximum:    {stats.loc[column, 'max']:.2f}")