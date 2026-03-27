# pip install streamlit
# streamlit run cwpc_basic.py

import streamlit as st

# page title
st.title("welcome to codeswithpankaj.com")
st.header("Welcome to Machine Learning")

# simple text
st.write("For beginners and real projects → Use Spring Boot + JPA (less code, everything is automatic.Learn Pure Hibernate only when you want to understand how things work internally.")

# input from user 
name = st.text_input("Enter Your Name - ")

if st.button("Result"):
    st.success(f"Hello {name or 'Friend'}!")
    
    
# display chart
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
)   

st.line_chart(chart_data)

st.caption("this is demo chart...") 


name1 = st.text_input("Enter Your Name")
age = st.number_input("Your Age ",min_value=0,max_value=120)

# slider and selectors 
value = st.slider("Pick a value ",0,100,50)
option = st.selectbox("choose one",['mumbai','pune','surat'])
options = st.multiselect("choose multiple ",['apple','banana','cherry'])

if st.button('click'):
    st.balloons()
    
if st.checkbox("show advance option"):
    st.write("advance ...")    
    
    

    