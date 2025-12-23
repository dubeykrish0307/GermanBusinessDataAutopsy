# German Business Data Autopsy

## Project Overview
This project analyzes official German retail turnover data to understand how retail business performance changes over time, particularly under inflationary conditions.

Using publicly available data from the German Federal Statistical Office (Destatis), the analysis distinguishes between nominal turnover (current prices) and real turnover (inflation-adjusted) to avoid misleading interpretations of revenue growth.

## Key Questions
- How has German retail turnover evolved over time?
- When does nominal revenue growth diverge from real business performance?
- Are there periods of abnormal decline that may signal business risk?

## Data Source
- German Federal Statistical Office (Destatis)
- Dataset: Retail trade turnover index (semi-annual)

## Methodology
- Cleaned and structured semi-annual time series data
- Converted period-based data into explicit datetime representation
- Compared nominal and real turnover trends
- Identified abnormal declines using year-over-year analysis
- Interpreted results in a business decision-making context

## Key Insights
- Nominal turnover growth does not always reflect real business growth
- Periods of divergence between nominal and real turnover highlight inflationary pressure
- Significant declines in real turnover may indicate heightened business risk

## Business Relevance
This analysis demonstrates how publicly available aggregate data can support informed business decisions, especially when operating under uncertainty and inflation.

## Tools Used
- Python
- pandas
- matplotlib

## Disclaimer
This project uses aggregated public data and does not establish causal relationships. The insights are intended to support exploratory analysis and decision-making, not precise forecasting.
