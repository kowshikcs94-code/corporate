import plotly.express as px

industry = (
    df.groupby("industry")
    .agg({
        "ai_adoption_level":"mean",
        "revenue_impact":"mean"
    })
    .reset_index()
)

fig = px.bar(
    industry,
    x="industry",
    y="ai_adoption_level",
    color="revenue_impact",
    title="Industry AI Adoption"
)

st.plotly_chart(fig)
