country_df = (
    df.groupby("country")
    .agg({
        "ai_adoption_level":"mean",
        "revenue_impact":"mean"
    })
    .reset_index()
)

fig = px.choropleth(
    country_df,
    locations="country",
    locationmode="country names",
    color="ai_adoption_level",
    hover_name="country"
)

st.plotly_chart(fig)
