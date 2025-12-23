def generate_business_insights(df):
    insights = []

    for date, row in df.iterrows():

        # Rule 1: Margin pressure
        if (
            row["real_yoy_change"] < 0
            and row["electricity_price_index"] > df["electricity_price_index"].mean()
        ):
            insights.append(
                f"{date.date()}: Margin pressure risk — real sales declined while energy costs were elevated."
            )

        # Rule 2: Illusory growth
        if (
            row["inflation_gap"] > df["inflation_gap"].mean()
            and row["real_yoy_change"] <= 0
        ):
            insights.append(
                f"{date.date()}: Illusory growth — nominal turnover increased mainly due to price effects."
            )

        # Rule 3: Healthy growth
        if (
            row["real_yoy_change"] > 3
            and row["electricity_price_index"] <= df["electricity_price_index"].mean()
        ):
            insights.append(
                f"{date.date()}: Healthy growth — real demand increased without significant cost pressure."
            )

        # Rule 4: Demand shock
        if row["real_yoy_change"] < -5:
            insights.append(
                f"{date.date()}: Demand shock — significant contraction in real retail activity."
            )

    return insights
