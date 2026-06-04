fig = px.histogram(
    df,
    x="ai_maturity_score",
    nbins=30,
    title="AI Maturity Distribution"
)

st.plotly_chart(fig)
