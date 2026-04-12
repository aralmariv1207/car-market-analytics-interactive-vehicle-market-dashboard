import pandas as pd
import streamlit as st
import plotly.express as px

st.header("Car Sales Analysis Dashboard")

# Optimization: Using cache so the app doesn't reload the CSV on every interaction
@st.cache_data
def load_data():
    return pd.read_csv('data/vehicles_us.csv')

df = load_data()

# --- Visualizations ---

st.write("### Price Distribution by Model Year")
fig_scatter = px.scatter(df, x='price', y='model_year', title="Price vs. Year")
st.plotly_chart(fig_scatter, use_container_width=True)

st.write("### Vehicle Condition Analysis")
show_hist = st.checkbox("Show Histogram of Prices")

if show_hist:
    fig_hist = px.histogram(df, x='price', title="Distribution of Vehicle Prices")
    st.plotly_chart(fig_hist, use_container_width=True)
    
