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
- [Contributing](#contributing)
- [License & citation](#license--citation)
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
1. Get the data:
   - Download: script or link, e.g., scripts/download_data.sh
   - Or: instructions to request credentials if private
2. Preprocess:
   - python src/preprocess.py --input data/raw --output data/processed
3. Run analysis:
   - python src/run_analysis.py --config config/config.yml
4. Recreate figures:
   - python src/plot_results.py --results results/ --out results/figures
5. Jupyter notebooks:
   - jupyter lab notebooks/ (notebooks are ordered; run 01_prepare_data.ipynb first)

Replace commands above with the exact commands your project uses.

## **Code layout**
- notebooks/01_exploration.ipynb — exploratory analysis
- src/data.py — data loading and preprocessing functions
- src/models.py — model training and evaluation
- src/utils.py — helper functions
- scripts/ — convenience scripts for running the pipeline
- results/ — final outputs and figures

## **Results**
- Brief highlights of the main findings.
- Link to key figures: results/figure_main.png
- If you have an HTML report or dashboard, link to it.

## **Limitations & ethics**
- Known limitations and assumptions (small sample sizes, biases, missingness).
- Privacy or ethical considerations (PII removed? anonymized?).
- If data are sensitive: state that raw data are not included and describe how to access.

## **Tests & validation**
- How results were validated (cross-validation, holdout set).
- How to run unit tests (if any):
  - pytest tests/

## **Contributing**
- How to raise issues or PRs.
- Code style and testing expectations.

## **License & citation**
- License: e.g., MIT / CC-BY / proprietary
- How to cite this work (provide citation, DOI, or BibTeX).

## **Contact**
- Maintainer: Aidan Chow (GitHub: @Ai-C-12, email: chow.aidanl@gmail.com)
