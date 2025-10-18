# **🏀 NBA Evolution of Strategy (2000–2025)**

This project analyzes how NBA team strategies have evolved over the past two decades using data from the official [NBA Stats API](https://github.com/swar/nba_api).  
It highlights major shifts in **pace, rebounding, defense, shooting efficiency, assists vs isolation, and the rise of the 3-point shot**.

## **Key Analyses**
We analyze NBA league basic counting data and advanced metric data from the official [NBA Stats API](https://github.com/swar/nba_api) to quantify changes in:</br>
 - **Pace & Possessions** → How tempo has changed across eras.</br>
 - **Rebounding Strategy** → Shift from offensive rebounding to transition defense.</br>
 - **Defense Trends** → Defensive rating, steals, and blocks over time.</br>
 - **Scoring Efficiency** → Effective FG% and True Shooting% trends.</br>
 - **Assists vs Isolation** → Team ball vs isolation baskets.</br>
 - **3PT Evolution** → The growth of 3-point attempts and efficiency.</br>


## **Table of contents**
- [Motivation](#motivation)
- [Data](#data)
- [Methods](#methods)
- [Reproducibility](#reproducibility)
- [Usage](#usage)
- [Code layout](#code-layout)
- [Results](#results)
- [Limitations & ethics](#limitations--ethics)
- [Contact](#contact)

## **Motivation**
Short background and the research question(s) being answered.

## **Data**
- **Source(s):** NBA Stats API (accessed via Python requests or nba_api library).
- **License:** e.g., CC-BY, proprietary, etc.
- **Size:**
   - **Rows:** One entry per team per season (≈30 teams × ~30 seasons = ~900 rows).
   - **Columns:** 42 total, including advanced metrics and identifiers such as season, team_id, pace, efg%, ts%, def_rating, orb%, drb%, 3pa, and 3p%.
- **Data dictionary:** 
   - SEASON: Year or range representing the NBA season (e.g., 2023–24).
   - team: Team name.
   - pace: Possessions per 48 minutes (game tempo).
   - efg%: Effective field goal percentage (shooting efficiency).
   - ts%: True shooting percentage (overall scoring efficiency).
   - def_rating: Points allowed per 100 possessions.
   - orb% / drb%: Offensive and defensive rebounding rates.
   - 3pa / 3p%: 3-point attempts and accuracy.
   (Full data dictionary in data_dictionary.md)

## **Methods (brief)**
- Preprocessing steps: e.g., missing-value handling, normalization, filtering rules.
- Modeling / analysis: e.g., regression, random forest, hypothesis tests, packages used.
- Key hyperparameters or settings.

## **Reproducibility**
Environment:
- Included file: environment.yml (conda) or requirements.txt (pip)
- Example (conda):
  - conda env create -f environment.yml
  - conda activate myproject
- Or (pip):
  - python -m venv venv
  - source venv/bin/activate
  - pip install -r requirements.txt

Optional: Dockerfile or Binder link (if provided).

## **Usage — step-by-step**
### 1. Download raw data from NBA api (Seasons 2000-25):
```bash
python script/fetch_data.py
```
This will save the following CSVs in data/raw:
- basic_NBA_data.csv
- advanced_NBA_data.csv

### 2. Preprocess:
```bash
python script/preprocess.py --input data/raw --output data/processed
```
This will clean the data by removing NaN values and filling counting statistics with 0.

### 3. Plot Figures:
```bash
python script/plot.py
```
Plots out some graphs to show trends.

## **Code layout**
<pre>
NBA-Evolution-Analysis/
│
├── data/
│   ├── raw/
│   │   ├── basic_NBA_data.csv
│   │   └── advanced_NBA_data.csv
│   └── processed/
│       └── NBA_processed_combined_data.csv
│
├── notebooks/
|   └──NBA_data.ipynb
|
├── outputs/
│   ├── 3-Point Efficiency.png
│   ├── Assists vs Iso.png
│   ├── Defense.png
│   ├── Pace vs Possessions.png
│   ├── Rebounding Strategy (Every 5 Seasons).png
│   └── Scoring Efficiency.png
|
├── script/
│   ├── fetch_data.py
│   ├── preprocess.py
│   └── plot.py
│
├── Analysis.md
├── Data_dictionary.md
├── README.md
└── requirements.txt
</pre>

## **Results**

### Pace vs Possessions
[Pace vs Possessions](output/Pace vs Possessions.png)

### Rebounding Strategy
[Rebounding](output/Rebounding Strategy (Every 5 Seasons).png)

### Defensive Trends
[Defense](output/Defense.png)

### Scoring Efficiency
[Scoring Efficiency](output/Scoring Efficiency.png)

### Assisted vs Isolation Baskets
[Assist vs Iso](output/Assists vs Iso.png)

### 3-Point Evolution
[3-Point Efficiency](output/3-Point Efficiency.png)

Further Insights:
Dashboard link***

## **Limitations & ethics**
- Known limitations and assumptions (small sample sizes, biases, missingness).
- Privacy or ethical considerations (PII removed? anonymized?).
- If data are sensitive: state that raw data are not included and describe how to access. 

## **Contact**
- Maintainer: Aidan Chow (GitHub: @Ai-C-12, email: chow.aidanl@gmail.com)
