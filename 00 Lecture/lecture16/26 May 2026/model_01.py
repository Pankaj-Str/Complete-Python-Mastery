# pip install streamlit
# run file --
# streamlit run model_01.py

import streamlit as st

st.set_page_config(page_title="Learning Path")
# set page title 
st.title("This is my First model ML 01")

st.write("""A faster way to build and share data apps
Turn your data scripts into shareable web apps in minutes.
All in pure Python. No front‑end experience required.""")

# header 
st.header("Learning Path")

# text input 
name = st.text_input("What is your name ","type here...")
# slider 
age = st.slider("Select Your age ?",0,100,25)
# select box 
color = st.selectbox(
    "what is your favorite color ?",
    ["Red","Blue","Green","Yellow","Purple"]
)
# button 
if st.button("Get Info"):
    st.success(f"hello {name}")
    st.info(f"your age is {age} and your favorite color is {color}")
    # st.balloons()
    st.snow()
else:
    st.success("plz enter all value info...")    
    
    
import numpy as np
import pandas as pd

data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["Mumbai","Pune","Surat"]
)  

st.line_chart(data)

# footer

st.markdown("---")
st.caption("Create by rupali - Machine Learning Development")  
