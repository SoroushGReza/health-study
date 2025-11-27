# Hälsostudie – Individuell Uppgift

Detta repository innehåller min individuella analys av ett hälsostudiedataset, genomförd i två delar enligt kursens instruktioner.  
Analysen utförs i Python i en Jupyter Notebook och körs i Visual Studio Code på Windows.

---

## 📁 Projektstruktur

```text
health-study/
│
├── data/
│   └── health_study_dataset.csv
│
├── images/
│   ├── histogram_bp.png
│   ├── boxplot_weight_sex.png
│   ├── smokers_barplot.png
│   ├── regression_pred_vs_actual.png
│   └── disease_by_sex.png
│
├── notebooks/
│   ├── health_study_del1.ipynb
│   ├── health_study_del2.ipynb
│
├── src/   
│   ├── data_loading.py
│   ├── statistics.py
│   ├── visualization.py
│   └── health_analyzer.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧪 Del 1 – Grundläggande analys & statistik

Notebook:  
`notebooks/health_study_del1.ipynb`

Del 1 innehåller:

### ✔️ Beskrivande statistik
- Medelvärde, median, min och max för:
  - ålder  
  - vikt  
  - längd  
  - systoliskt blodtryck  
  - kolesterol  

### ✔️ Visualiseringar
Minst tre grafer (krav uppfyllt):
- Histogram över systoliskt blodtryck  
- Boxplot över vikt per kön  
- Stapeldiagram över andelen rökare  

## 📊 Visualiseringar (bilder)

### Histogram över systoliskt blodtryck
<img src="./images/histogram_bp.png" width="400">

### Vikt per kön (boxplot)
<img src="./images/boxplot_weight_sex.png" width="400">

### Andel rökare
<img src="./images/smokers_barplot.png" width="400">



### ✔️ Simulering
- Räkning av sjukdomsandel i datasetet  
- Simulering av 1000 slumpade personer med motsvarande sannolikhet  
- Jämförelse mellan verklig och simulerad sjukdomsförekomst  

### ✔️ Konfidensintervall
Beräkning av 95% konfidensintervall för systoliskt blodtryck med två metoder:
- Normalapproximation  
- Bootstrap  

### ✔️ Hypotesprövning
Test av hypotesen:
> **”Rökare har högre medelblodtryck än icke-rökare.”**  
Genomfört med:
- Welch’s t-test (ensidigt)

Markdown med tolkning inkluderad.

### ✔️ Power-simulering
Simulering av 1000 studier för att uppskatta testets power:
- Hur ofta ett t-test hittar en verklig skillnad  
- Diskussion om resultatet och metodval  

---


## 🧬 Del 2 – Fördjupning & Pipeline

Notebook:  
`notebooks/health_study_del2.ipynb`

Del 2 innehåller:

### ✔️ Kodstrukturering
- Koden från del 1 har flyttats till separata moduler i `src/`:
  - `data_loading.py`
  - `statistics.py`
  - `visualization.py`
  - `health_analyzer.py`

### ✔️ HealthAnalyzer-klass
En objektorienterad klass som:
- hanterar beskrivande statistik  
- ritar visualiseringar  
- utför multipel linjär regression  
- genererar diagnostiska grafer  
- ger en grund för vidare analyser

### ✔️ Multipel linjär regression
Blodtryck modelleras som funktion av både ålder och vikt.  
Regressionen bygger på linjär algebra:  
\[
\hat{\beta} = (X^TX)^{-1}X^Ty
\]

### ✔️ Diagnostisk visualisering
Plottet nedan jämför observerat vs. förutsagt blodtryck:

<img src="./images/regression_pred_vs_actual.png" width="400">

### ✔️ Extra analys: sjukdomsförekomst per kön
Visar hur vanligt sjukdomen är bland kvinnor och män:

<img src="./images/disease_by_sex.png" width="400">

---

## 🔄 Reproducerbarhet

För att notebooken ska köras identiskt:

- Data läses in via relativ sökväg  
  `../data/health_study_dataset.csv`
- Slump-seed sätts i början av notebooken:  
  ```python
  import numpy as np
  np.random.seed(42)
  ```
---
 ## 🛠 Teknisk miljö

- Python-version: 3.11

**Miljö**: 
Virtuell miljö .venv (exkluderad via .gitignore)

**Editor**: 
Visual Studio Code

**Bibliotek**:

- dataclasses
- numpy
- pandas
- matplotlib
- seaborn
- scipy
- scikit-learn
- jupyter
