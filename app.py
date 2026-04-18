import streamlit as st
import pandas as pd
import numpy as np
import joblib

# MUST BE FIRST
st.set_page_config(page_title="Retail Dashboard", layout="wide")

# Custom CSS (Dark UI + Cards)
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0e1117;
}
h1 {
    font-size: 40px !important;
    font-weight: 700 !important;
}
[data-testid="metric-container"] {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #2c2f36;
}
[data-testid="stSidebar"] {
    background-color: #161a23;
}
</style>
""", unsafe_allow_html=True)

# Imports (your modules)
from src.preprocess import load_data, clean_data, add_time_features
from src.features import create_features
from src.inventory import calculate_inventory

# Load data
df = load_data("data/data.csv")
df = clean_data(df)
df = add_time_features(df)
df = create_features(df)

# Load model
model = joblib.load("models/model.pkl")

# Title
st.title("📈 Retail Sales Forecasting & Inventory Dashboard")
st.markdown("### AI-driven demand prediction and inventory optimization")

# Sidebar
st.sidebar.title("⚙️ Input Parameters")
st.sidebar.markdown("---")

product = st.sidebar.selectbox("Select Product", df["product_id"].unique())
current_stock = st.sidebar.number_input("Current Stock", value=150)
day = st.sidebar.slider("Day", 1, 31, 15)
month = st.sidebar.slider("Month", 1, 12, 6)

# Select product-specific data
sample = df[df["product_id"] == product].iloc[-1:].copy()

# Modify input
sample["day_of_week"] = day % 7
sample["month"] = month

X = sample.drop(["date", "product_id", "qty_sold"], axis=1)

# Prediction
pred = model.predict(X)[0]

# Inventory calculation
inventory = calculate_inventory([pred]*7, on_hand=current_stock)

# Metrics Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📊 Forecast Sales", round(pred, 2))

with col2:
    st.metric("📦 Current Stock", current_stock)

with col3:
    st.metric("⚠️ Reorder Point", round(inventory["reorder_point"], 2))

with col4:
    st.metric("🛒 Recommended Order", round(inventory["order_quantity"], 2))

# Chart
st.subheader("📉 Model Performance")

chart_data = pd.DataFrame({
    "Actual": df[df["product_id"] == product]["qty_sold"].tail(50).values,
    "Predicted": model.predict(
        df[df["product_id"] == product]
        .drop(["date", "product_id", "qty_sold"], axis=1)
        .tail(50)
    )
})

st.line_chart(chart_data, height=350)
st.caption("Blue = Actual | Orange = Predicted")

# Download Section
st.markdown("### 📥 Download Results")

results_df = pd.DataFrame({
    "Product": [product],
    "Forecast": [round(pred, 2)],
    "Reorder Point": [round(inventory["reorder_point"], 2)],
    "Order Quantity": [round(inventory["order_quantity"], 2)]
})

st.download_button(
    label="Download CSV",
    data=results_df.to_csv(index=False),
    file_name="forecast_output.csv",
    mime="text/csv"
)