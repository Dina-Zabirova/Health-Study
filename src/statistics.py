import pandas as pd
import numpy as np
from math import sqrt
from scipy import stats

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



def ci_mean_normal(x):
    """
    Beräknar ett 95-procentigt konfidensintervall för medelvärdet
    med hjälp av normalapproximation.
    """
    mean_x = np.mean(x)                                              # Beräknar medelvärde, standardavvikelse och stickprovsstorlek
    s = np.std(x, ddof=1)
    n = len(x)

    z_critical = 1.96                                                # Beräknar felmarginalen för ett 95-procentigt konfidensintervall
    half_width = z_critical * s / sqrt(n)

    lo = mean_x - half_width                                         # Beräknar konfidensintervallets gränser
    hi = mean_x + half_width

    return lo, hi, mean_x, s, n


def ci_mean_bootstrap(x, B=1000, confidence=0.95, seed=89):
    """
    Beräknar ett bootstrap-konfidensintervall för medelvärdet.
    """
    rng = np.random.default_rng(seed)                                 # Skapar en slumpgenerator med ett fast seed
    n = len(x)                                                        # Bestämmer stickprovsstorleken och skapar en tom array
    boot_means = np.empty(B)

    for b in range(B):                                                # Skapar bootstrap-stickprov och beräknar medelvärden
        boot_sample = rng.choice(x, size=n, replace=True)
        boot_means[b] = np.mean(boot_sample)

    alpha = (1 - confidence) / 2                                      # Beräknar konfidensintervallets nedre och övre gräns
    lo, hi = np.percentile(
        boot_means,
        [100 * alpha, 100 * (1 - alpha)]
    )

    return lo, hi, float(np.mean(x))



def test_smoking_blood_pressure(df):
    """
    Undersöker om rökare har högre genomsnittligt systoliskt
    blodtryck än icke-rökare med ett ensidigt Welch's t-test.

    Returnerar gruppernas medelvärden, skillnaden,
    t-statistiken och p-värdet.
    """
    smokers_bp = df.loc[df["smoker"] == "Yes", "systolic_bp"]           # Delar upp blodtrycksvärdena i två grupper
    non_smokers_bp = df.loc[df["smoker"] == "No", "systolic_bp"]

    mean_smokers = smokers_bp.mean()                                    # Beräknar medelvärdet för varje grupp
    mean_non_smokers = non_smokers_bp.mean()

    mean_difference = mean_smokers - mean_non_smokers                   # Beräknar skillnaden mellan gruppernas medelvärden

    t_stat, p_value = stats.ttest_ind(                                  # Genomför ett ensidigt Welch's t-test
        smokers_bp,
        non_smokers_bp,
        equal_var=False,
        alternative="greater"
    )

    return mean_smokers, mean_non_smokers, mean_difference, t_stat, p_value



def simulate_test_power(df, effect=5, n_simulations=1000, seed=89):
    """
    Uppskattar styrkan hos ett ensidigt Welch's t-test
    genom simulering med en förutbestämd skillnad i medelblodtryck.
    """
    smokers_bp = df.loc[df["smoker"] == "Yes", "systolic_bp"]                   # Delar upp blodtrycksvärdena i två grupper
    non_smokers_bp = df.loc[df["smoker"] == "No", "systolic_bp"]

    n_smokers = len(smokers_bp)                                                 # Hämtar gruppernas storlek och standardavvikelse
    n_non_smokers = len(non_smokers_bp)

    std_smokers = smokers_bp.std()
    std_non_smokers = non_smokers_bp.std()

    mean_non_smokers = non_smokers_bp.mean()                                    # Anger medelvärden med en förutbestämd skillnad
    mean_smokers = mean_non_smokers + effect

    rng = np.random.default_rng(seed)                                           # Skapar en slumpgenerator

    significant_tests = 0                                                       # Räknar antalet signifikanta test

    for _ in range(n_simulations):
        simulated_smokers = rng.normal(                                         # Simulerar blodtryck för båda grupperna
            loc=mean_smokers,
            scale=std_smokers,
            size=n_smokers
        )

        simulated_non_smokers = rng.normal(
            loc=mean_non_smokers,
            scale=std_non_smokers,
            size=n_non_smokers
        )

        t_stat, p_value = stats.ttest_ind(                                      # Genomför samma ensidiga t-test som tidigare
            simulated_smokers,
            simulated_non_smokers,
            equal_var=False,
            alternative="greater"
        )

        if p_value < 0.05:                                                      # Räknar test som hittar en signifikant skillnad
            significant_tests += 1

    power = significant_tests / n_simulations                                   # Beräknar testets uppskattade styrka

    return power