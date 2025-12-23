# German Business Data Autopsy 🇩🇪

A business-focused analysis of German retail performance under inflation and energy cost pressure, built using official German and EU datasets.  
This project goes beyond charts by translating economic data into clear, decision-relevant business insights.

---

PROJECT MOTIVATION

During inflationary periods, nominal revenue growth can be misleading.  
Businesses may appear to grow on paper while real demand stagnates or declines and operating costs rise.

This project answers a simple but critical question:

Are German retail businesses genuinely growing, or is growth merely an inflation illusion?

To answer this, the analysis combines:
- Nominal vs real retail turnover
- Business electricity cost indicators
- A rule-based insight engine that mimics real analyst reasoning

---

DATA SOURCES

Retail Turnover Data  
Source: German Federal Statistical Office (Destatis)  
Dataset: Retail trade turnover index (semi-annual)

Metrics used:
- Nominal turnover (current prices)
- Real turnover (inflation-adjusted)

Energy Cost Data  
Source: Eurostat  
Dataset: Electricity prices for non-household consumers  
Purpose: Proxy for operating cost pressure on businesses

All datasets used are official, public, and reproducible.

---

METHODOLOGY OVERVIEW

Step 1 — Data Cleaning & Structuring  
- Parsed semi-annual time periods (S1, S2) into consistent datetime format  
- Preserved raw indicators to ensure auditability  
- Aggregated duplicate statistical observations correctly  

Step 2 — Nominal vs Real Performance Analysis  
- Compared nominal and real turnover to detect inflation-driven distortions  
- Computed an inflation gap to quantify misleading growth  

Step 3 — Cost Pressure Integration  
- Cleaned and aggregated business electricity price indices  
- Aligned energy costs with retail turnover timelines  
- Ensured consistent time granularity across datasets  

Step 4 — Rule-Based Insight Engine  
Instead of stopping at visualizations, explicit business rules convert data into actionable insights:
- Margin pressure risk
- Illusory growth
- Demand shocks
- Healthy growth regimes

---

RULE-BASED INSIGHT ENGINE (CORE FEATURE)

The insight engine converts economic signals into plain-English business interpretations using transparent logic.

Key rules include:
- Margin pressure risk: real demand declines while energy costs are elevated
- Illusory growth: nominal turnover rises but real turnover stagnates or falls
- Demand shock: large year-over-year contraction in real activity
- Healthy growth: real demand rises without significant cost pressure

This mirrors how consultants and analysts evaluate businesses in practice.

---

EXAMPLE OUTPUT

Running the insight engine produces results such as:

    2020-07-01: Healthy growth — real demand increased without significant cost pressure.
    2021-01-01: Demand shock — significant contraction in real retail activity.
    2023-07-01: Margin pressure risk — real sales declined while energy costs were elevated.
    2023-07-01: Illusory growth — nominal turnover increased mainly due to price effects.

Multiple insights for the same period indicate compounded business stress, not an error.

---

REPOSITORY STRUCTURE

    GermanBusinessDataAutopsy/
    ├── data/
    │   ├── raw/
    │   │   ├── DESTATIS-45212BH002.csv
    │   │   └── energy_prices_non_household.csv
    │   └── processed/
    │       └── energy_price_index.csv
    ├── notebooks/
    │   ├── 01_data_ingestion.ipynb
    │   └── 02_energy_data_ingestion.ipynb
    ├── src/
    │   ├── __init__.py
    │   └── insight_engine.py
    ├── requirements.txt
    └── README.md

---

HOW TO RUN THE PROJECT

1. Clone the repository

    git clone https://github.com/dubeykrish0307/GermanBusinessDataAutopsy.git
    cd GermanBusinessDataAutopsy

2. Create a virtual environment (recommended)

    python -m venv venv
    source venv/bin/activate      (macOS / Linux)
    venv\Scripts\activate         (Windows)

3. Install dependencies

    pip install -r requirements.txt

4. Run the notebooks in order

    notebooks/02_energy_data_ingestion.ipynb
    notebooks/01_data_ingestion.ipynb

The second notebook merges datasets and runs the rule-based insight engine.

---

BUSINESS RELEVANCE

This project demonstrates:
- Why nominal growth alone is misleading
- How inflation distorts perceived performance
- How energy cost shocks amplify risk
- Why explainable logic often beats black-box models

---

WHY RULE-BASED INSTEAD OF MACHINE LEARNING

The goal is interpretability, not raw prediction accuracy.  
Business decisions require transparent logic that stakeholders can understand and challenge.

Machine learning could be layered later, but only after understanding the economic fundamentals.

---

LIMITATIONS AND FUTURE WORK

Limitations:
- Aggregated national-level data
- No firm-specific cost structures

Future extensions:
- Add labor or wage cost indices
- Analyze retail sub-sectors separately
- Introduce severity scoring for risk regimes
- Evaluate predictive models on top of rule-based insights

---

AUTHOR

Developed by Krish  
Bachelor’s student in Computer Science with a strong interest in data-driven business analysis and economic decision support.
