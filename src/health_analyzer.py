import matplotlib.pyplot as plt

class HealthAnalyzer:
    def __init__(self, df):
        """
        Initierar analysatorn med ett DataFrame.
        """
        self.df = df

    def age_by_sex(self):
        """
        Beräknar medelåldern för kvinnor och män
        och returnerar resultatet.
        """
        mean_age_by_sex = self.df.groupby("sex")["age"].mean()
        return mean_age_by_sex

    def plot_age_by_sex(self):
        """
        Visualiserar medelåldern för kvinnor och män
        med hjälp av ett stapeldiagram.
        """
        mean_ages = self.age_by_sex()
        bars = plt.bar(
        mean_ages.index,
        mean_ages.values,
        color=["#81B29A", "#669BBC"]
        )
        plt.bar_label(bars, fmt="%.2f", padding=3)
        plt.ylim(0, 60)
        plt.xticks(["F", "M"], ["Kvinnor", "Män"])
        plt.xlabel("Kön")
        plt.ylabel("Medelålder (år)")
        plt.title("Medelålder efter kön")

        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.gca().set_axisbelow(True)

        plt.show()

    def blood_pressure_by_age(self):
        """
        Visualiserar sambandet mellan ålder och
        systoliskt blodtryck med hjälp av ett spridningsdiagram.
        """
        x = self.df["age"]
        y = self.df["systolic_bp"]
        plt.scatter(x, y, color="#669BBC", marker="o", alpha=0.5, s=20)
        plt.xlabel("Ålder (år)")
        plt.ylabel("Systoliskt blodtryck (mmHg)")
        plt.title("Samband mellan ålder och systoliskt blodtryck")
        plt.grid(linestyle="--", alpha=0.3)
        plt.gca().set_axisbelow(True)
        plt.show()

    def disease_by_smoking(self):
        """
        Beräknar andelen personer med sjukdom
        bland rökare och icke-rökare.
        """
        disease_rates = self.df.groupby("smoker")["disease"].mean() * 100
        return disease_rates

    def plot_disease_by_smoking(self):
        """
        Visualiserar andelen personer med sjukdom
        bland rökare och icke-rökare med hjälp av
        ett stapeldiagram.
        """
        mean_rates = self.disease_by_smoking()
        bars = plt.bar(
        mean_rates.index,
        mean_rates.values,
        color=["#81B29A", "#669BBC"]
        )
        plt.bar_label(bars, fmt="%.2f%%", padding=3)
        plt.ylim(0, mean_rates.max() * 1.2)
        plt.xticks(["No", "Yes"], ["Icke-rökare", "Rökare"])
        plt.ylabel("Andel med sjukdom (%)")
        plt.title("Sjukdomsförekomst efter rökstatus")
        
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.gca().set_axisbelow(True)
        
        plt.show()