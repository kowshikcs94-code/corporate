import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Corporate AI Analytics",
    page_icon="🤖",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/corporate_ai_adoption_dataset.csv"
    )

df = load_data()

st.title("🤖 Corporate AI Adoption Intelligence Platform")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Companies",
    f"{len(df):,}"
)

col2.metric(
    "Countries",
    df.country.nunique()
)

col3.metric(
    "Industries",
    df.industry.nunique()
)

col4.metric(
    "Avg AI Adoption",
    round(df.ai_adoption_level.mean()*100,2)
)

st.divider()

country = st.selectbox(
    "Select Country",
    ["All"] + sorted(df.country.unique())
)

if country != "All":
    df = df[df.country == country]

fig = px.scatter(
    df.sample(5000),
    x="ai_investment_usd",
    y="revenue_impact",
    color="industry",
    size="deployment_count",
    title="Investment vs Revenue Impact"
)

st.plotly_chart(fig,use_container_width=True)
