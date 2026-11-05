import streamlit as st
import pandas as pd
import numpy as np

st.title("Simple Sales Dashboard")

# side bar 
st.sidebar.header("Filters")
year = st.sidebar.selectbox("year",[2023,2024,2025])

# data 
data = pd.DataFrame(
    {
        "Month":["Jan","Feb","Mar","Apr"],
        "Sales": np.random.randint(100,1000,4),
        "Profit":np.random.randint(50,500,4),
    }
)


st.dataframe(data)
col1,col2 = st.columns(2)
col1.metric("Total Sales : ",f"${data['Sales'].sum():,}")
col2.metric("Avg Profit : ",f"${data['Profit'].mean():.0f}")

st.bar_chart(data.set_index('Month')['Sales'])





