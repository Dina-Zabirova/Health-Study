# Hälsostudie – Dataanalys med Python

## Projektbeskrivning

Detta projekt är en individuell uppgift inom kursen *Pythonprogrammering och statistisk dataanalys*.

Syftet är att analysera ett dataset med hälsouppgifter och undersöka fördelningar, samband och statistisk osäkerhet med hjälp av Python.

Datasetet innehåller 800 observationer med information om ålder, kön, längd, vikt, systoliskt blodtryck, kolesterolnivå, rökvanor och sjukdomsförekomst.

## Genomförda analyser – Del 1

- Datakontroll och beskrivande statistik.
- Visualisering av blodtryck, vikt och rökvanor.
- Simulering av sjukdomsförekomst.
- Beräkning av 95-procentiga konfidensintervall med normalapproximation och bootstrap.
- Hypotesprövning med ett ensidigt Welch's t-test för att undersöka om rökare har högre genomsnittligt systoliskt blodtryck än icke-rökare.
- Simulering av testets statistiska styrka (power).

## Teknik och bibliotek

- Python
- pandas
- NumPy
- Matplotlib
- SciPy
- Jupyter Notebook

## Projektstruktur

```text
Health-Study/
├── data/
│   └── health_study_dataset.csv
├── notebooks/
│   └── report.ipynb
├── src/
│   ├── data_processing.py
│   ├── statistics.py
│   └── viz.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation och körning

1. Klona projektet från GitHub.
2. Skapa och aktivera en virtuell Python-miljö.
3. Installera beroenden med `pip install -r requirements.txt`.
4. Öppna `notebooks/report.ipynb` i VS Code eller Jupyter.
5. Kör notebookens celler i ordning.

## Resultat

Analysen visar att det genomsnittliga systoliska blodtrycket är cirka 149,18 mmHg.

Hypotesprövningen visar ingen statistiskt signifikant skillnad som ger stöd för att rökare har högre genomsnittligt systoliskt blodtryck än icke-rökare (p = 0,3264).

Simuleringen av statistisk styrka visar att testet har hög förmåga att upptäcka större skillnader mellan grupperna, men lägre förmåga att upptäcka små skillnader.

## Fortsatt arbete

I Del 2 kommer projektet att vidareutvecklas med objektorienterad programmering, regressionsanalys och ytterligare visualiseringar.