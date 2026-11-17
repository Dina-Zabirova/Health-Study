import pandas as pd
import matplotlib.pyplot as plt

def plot_blood_pressure(df: pd.DataFrame) -> tuple[Figure, Axes]:
    """
    Skapar ett histogram över deltagarnas systoliska blodtryck.
    Visar även medelvärdet med en vertikal streckad linje.
    Returnerar figuren och axeln för vidare användning.
    """
    fig, ax = plt.subplots(figsize=(8, 6))                           # Skapar en figur och en axel
    mean_bp = df["systolic_bp"].mean()                               # Beräknar medelvärdet för systoliskt blodtryck

    ax.hist(df["systolic_bp"], bins=20, edgecolor="white")           # Skapar ett histogram med 20 intervall
    ax.axvline(                                                      # Markerar medelvärdet med en vertikal linje
        x=mean_bp,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Medelvärde: {mean_bp:.2f} mmHg"
    )

    ax.set_title("Fördelning av systoliskt blodtryck")               # Anger titel och axelrubriker
    ax.set_xlabel("Systoliskt blodtryck (mmHg)")
    ax.set_ylabel("Antal deltagare")
    ax.grid(True, axis="y", alpha=0.5)
    ax.legend()
    fig.tight_layout()
    return fig, ax


def plot_weight_by_sex(df: pd.DataFrame) -> tuple[Figure, Axes]:
    """
    Skapar ett boxplot och ett violinplot för att visa
    viktfördelningen bland kvinnor och män.
    Returnerar figuren och axlarna för vidare användning.
    """
    fig, axes = plt.subplots(                                       # Skapar en figur med två diagram bredvid varandra
        1, 2,
        figsize=(12, 6),
        sharey=True,
        layout="constrained"
    )

    weights = [
        df.loc[df.sex == "F", "weight"],                            # Väljer viktdata för kvinnor och män
        df.loc[df.sex == "M", "weight"]
    ]

    axes[0].boxplot(                                                # Skapar ett boxplot
        weights,
        tick_labels=["Kvinnor", "Män"],
        showmeans=True
    )
    axes[0].set_title("Boxplot")
    axes[0].set_ylabel("Vikt (kg)")
    axes[0].grid(True, axis="y", alpha=0.3)

    axes[1].violinplot(weights, showmeans=True)                     # Skapar ett violinplot
    axes[1].set_xticks([1, 2], ["Kvinnor", "Män"])
    axes[1].set_title("Violinplot")
    axes[1].grid(True, axis="y", alpha=0.3)

    fig.suptitle("Viktfördelning efter kön")
    return fig, axes


def plot_smoking_distribution(df: pd.DataFrame) -> tuple[Figure, Axes]:
    """
    Skapar ett stapeldiagram som visar andelen rökare
    och icke-rökare i procent.
    Returnerar figuren och axeln för vidare användning.
    """
    smoking_pct = (                                                 # Beräknar andelen rökare och icke-rökare i procent
        df["smoker"]
        .value_counts(normalize=True)
        .reindex(["No", "Yes"], fill_value=0)
        * 100
    )

    fig, ax = plt.subplots(figsize=(8, 6))                         
    bars = ax.bar(                                                  # Skapar ett stapeldiagram
        ["Icke-rökare", "Rökare"],
        smoking_pct.values,
        color=["steelblue", "coral"],
        edgecolor="white"
    )

    ax.set_title("Andelen rökare bland deltagarna")                 # Anger titel och axelrubriker
    ax.set_xlabel("Rökvanor")
    ax.set_ylabel("Andel deltagare (%)")
    ax.bar_label(bars, fmt="%.1f%%", padding=3)                     # Visar procentvärden ovanför staplarna
    ax.set_ylim(0, 100)
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_axisbelow(True)
    fig.tight_layout()
    return fig, ax


def plot_confidence_intervals(mean, normal_ci, bootstrap_ci):
    """
    Jämför 95-procentiga konfidensintervall
    beräknade med normalapproximation och bootstrap.
    """
    fig, ax = plt.subplots(figsize=(9, 4))

    intervals = [normal_ci, bootstrap_ci]                           # Anger konfidensintervallen
    labels = ["Normalapproximation", "Bootstrap"]
    colors = ["steelblue", "coral"]

    for i, (lo, hi) in enumerate(intervals):                        # Ritar intervallen och markerar medelvärdet
        ax.plot(
            [lo, hi], [i, i],
            color=colors[i],
            linewidth=4
        )

        ax.scatter(mean, i, color="black", zorder=3)

        ax.vlines(
            [lo, hi],
            ymin=i,
            ymax=2,
            colors=colors[i],
            linestyles="dashed",
            linewidth=1,
            alpha=0.7
        )
    ax.set_ylim(2, -0.5)
    ax.set_title("Jämförelse av 95 % konfidensintervall")
    ax.set_xlabel("Systoliskt blodtryck (mmHg)")
    ax.set_yticks([0, 1], labels)
    ax.grid(True, axis="x", alpha=0.3)
    fig.tight_layout()
    return fig, ax