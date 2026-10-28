def generate_business_insights(df):
    """Turn each half-year in df into plain-English findings using four simple rules."""
    avg_energy = df["electricity_price_index"].mean()
    avg_gap = df["inflation_gap"].mean()
    insights = []

    for date, row in df.iterrows():
        day = date.date()
        real_change = row["real_yoy_change"]
        energy = row["electricity_price_index"]

        if real_change < 0 and energy > avg_energy:
            insights.append(f"{day}: Margin pressure risk — real sales declined while energy costs were elevated.")

        if row["inflation_gap"] > avg_gap and real_change <= 0:
            insights.append(f"{day}: Illusory growth — nominal turnover increased mainly due to price effects.")

        if real_change > 3 and energy <= avg_energy:
            insights.append(f"{day}: Healthy growth — real demand increased without significant cost pressure.")

        if real_change < -5:
            insights.append(f"{day}: Demand shock — significant contraction in real retail activity.")

    return insights
