# Hälsostudie – Dataanalys med Python

## Projektbeskrivning

Detta projekt är en individuell uppgift inom kursen **Pythonprogrammering och statistisk dataanalys**.

Syftet är att analysera ett dataset med hälsouppgifter och undersöka fördelningar, samband och statistisk osäkerhet med hjälp av Python.

Datasetet innehåller 800 observationer med information om ålder, kön, längd, vikt, systoliskt blodtryck, kolesterolnivå, rökvanor och sjukdomsförekomst.

Projektet består av två delar som omfattar beskrivande statistik, statistisk inferens, objektorienterad programmering och regressionsanalys.

## Genomförda analyser – Del 1

- Datakontroll och beskrivande statistik.
- Visualisering av blodtryck, vikt och rökvanor.
- Simulering av sjukdomsförekomst.
- Beräkning av 95-procentiga konfidensintervall med normalapproximation och bootstrap.
- Hypotesprövning med ett ensidigt Welch's t-test för att undersöka om rökare har högre genomsnittligt systoliskt blodtryck än icke-rökare.
- Simulering av testets statistiska styrka (power).

## Genomförda analyser – Del 2

- Objektorienterad programmering för analys av hälsodata.
- Jämförelse av ålder mellan kvinnor och män.
- Analys av sambandet mellan ålder och systoliskt blodtryck.
- Jämförelse av sjukdomsförekomst mellan rökare och icke-rökare.
- Multipel linjär regression för att undersöka sambandet mellan ålder, vikt och systoliskt blodtryck.
- Beräkning av regressionskoefficienter med hjälp av matrisoperationer och normalekvationerna.
- Beräkning av predikterade värden, residualer och modellens förklaringsgrad (R²).
- Visualisering och tolkning av regressionsmodellens resultat.

## Teknik och bibliotek

- Python
- pandas
- NumPy
- Matplotlib
- SciPy
- Jupyter Notebook

## Projektstruktur

```
Health-Study/
├── data/
│   └── health_study_dataset.csv
├── notebooks/
│   ├── report.ipynb
│   └── report_del2.ipynb
├── src/
│   ├── data_processing.py
│   ├── statistics.py
│   ├── viz.py
│   ├── health_analyzer.py
│   └── regression.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation och körning

1. Klona projektet från GitHub.
2. Skapa och aktivera en virtuell Python-miljö.
3. Installera beroenden med `pip install -r requirements.txt`.
4. Öppna `notebooks/report.ipynb` för Del 1 eller `notebooks/report_del2.ipynb` för Del 2 i VS Code eller Jupyter.
5. Välj den virtuella Python-miljön som kernel.
6. Kör notebookens celler i ordning uppifrån och ned.

## Resultat

### Del 1

Analysen visar att det genomsnittliga systoliska blodtrycket är cirka 149,18 mmHg.

Hypotesprövningen visar ingen statistiskt signifikant skillnad som ger stöd för att rökare har högre genomsnittligt systoliskt blodtryck än icke-rökare (p = 0,3264).

Simuleringen av statistisk styrka visar att testet har hög förmåga att upptäcka större skillnader mellan grupperna, men lägre förmåga att upptäcka små skillnader.

### Del 2

Den observerade sjukdomsförekomsten är högre bland rökare (8,92 %) än bland icke-rökare (4,77 %). Resultatet tyder på ett möjligt samband mellan rökning och sjukdomsförekomst, men skillnadens statistiska signifikans har inte undersökts i denna analys.

Den multipla linjära regressionen visar positiva samband mellan ålder, vikt och systoliskt blodtryck.

Regressionsmodellens förklaringsgrad (R²) är 0,405, vilket innebär att modellen förklarar cirka 40,5 % av variationen i det systoliska blodtrycket i datasetet.

Residualdiagrammet visar inga tydliga systematiska mönster. En stor del av variationen förklaras dock inte av modellen, vilket innebär att även andra faktorer kan vara av betydelse.

Regressionsmodellen har anpassats och utvärderats på hela datasetet utan uppdelning i tränings- och testdata.