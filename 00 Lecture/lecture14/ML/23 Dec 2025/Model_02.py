# pip install streamlit
# pip install scikit-learn
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# page design 
st.set_page_config(
    page_title="Random Forest Classifier",
    page_icon="🌲",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("💀Random Forest Classifier ☠️🌲☠️")
st.markdown(
    """
    This app allows you to train a Random Forest Classifier on your dataset.
    - CWPC 2025
    - Developed by Your Name
    ### GitHub: pankaj_str
    """
)

