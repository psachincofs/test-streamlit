import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Sample App")

st.write("Welcome to the Streamlit sample app!")

# Sidebar
st.sidebar.header("Settings")
num_rows = st.sidebar.slider("Number of data points", min_value=10, max_value=200, value=50)
chart_type = st.sidebar.selectbox("Chart type", ["Line", "Bar", "Area"])

# Generate sample data
np.random.seed(42)
data = pd.DataFrame(
    {
        "x": range(num_rows),
        "y1": np.random.randn(num_rows).cumsum(),
        "y2": np.random.randn(num_rows).cumsum(),
    }
)

st.subheader("Sample Data")
st.dataframe(data.head(10))

st.subheader("Chart")
if chart_type == "Line":
    st.line_chart(data.set_index("x")[["y1", "y2"]])
elif chart_type == "Bar":
    st.bar_chart(data.set_index("x")[["y1", "y2"]])
else:
    st.area_chart(data.set_index("x")[["y1", "y2"]])

# User input section
st.subheader("Interactive Input")
name = st.text_input("Enter your name", "World")
st.write(f"Hello, {name}!")

if st.button("Show summary statistics"):
    st.write(data.describe())
