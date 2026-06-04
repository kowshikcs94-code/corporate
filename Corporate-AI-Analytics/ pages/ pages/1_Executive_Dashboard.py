import streamlit as st
import pandas as pd

df = pd.read_csv(
    "data/corporate_ai_adoption_dataset.csv"
)

st.title("Executive Dashboard")

roi = (
    df["revenue_impact"].sum()
    /
    df["ai_investment_usd"].sum()
)

st.metric(
    "AI ROI",
    f"{roi:.2f}x"
)

st.metric(
    "Average Cost Savings",
    f"${df.cost_savings.mean():,.0f}"
)

st.metric(
    "Average Productivity Gain",
    f"{df.productivity_gain.mean()*100:.1f}%"
)
