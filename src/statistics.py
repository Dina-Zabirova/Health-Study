import pandas as pd
import numpy as np

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



def simulate_disease(df, n_people=1000, seed=89):
    """
    Simulerar sjukdomsförekomst baserat på andelen sjuka
    i det ursprungliga datasetet.

    Returnerar den ursprungliga sjukdomsandelen,
    antalet sjuka och andelen sjuka i simuleringen.
    """

    disease_probability = df["disease"].mean()                      # Beräknar andelen sjuka i det ursprungliga datasetet
    
    rng = np.random.default_rng(seed)                               # Skapar en slumpgenerator med ett fast seed

    simulated_disease = rng.binomial(                               # Simulerar sjukdomsförekomst för ett angivet antal personer
        n=1,
        p=disease_probability,
        size=n_people
    )

    simulated_count = simulated_disease.sum()                       # Beräknar antalet sjuka i simuleringen
    simulated_probability = simulated_disease.mean()                # Beräknar andelen sjuka i simuleringen

    return disease_probability, simulated_count, simulated_probability # Returnerar resultaten