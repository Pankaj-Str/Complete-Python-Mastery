# pip install streamlit
# streamlit run Model.py
import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🏥",
    layout="centered"
)

# title and intro
st.title("BMI Calculator")
st.write("Free Body Mass Index calculator gives out the BMI value and categorizes BMI based on provided information from WHO and CDC for both adults and children.")

# input section
st.subheader("Enter Your Details")

# using 2 columns 
col1 , col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg)",min_value=1.0,value=70.0,step=1.5)

with col2:
    height = st.number_input("Height (m)",min_value=0.5,value=1.7,step=0.01,max_value=2.5)

if st.button("Calculate BMI",type="primary",use_container_width=True):
    if height > 0:
        bmi = weight /(height**2) 
        # show result 
        st.success(f"Your BMI is {bmi:.2f}")

        if bmi < 18.5:
            st.warning("🟡 Under weight 🟡")
        elif bmi < 25:
            st.success("🟢 Normal weight 🟢")
        elif bmi < 30:
            st.warning("🟠 Over Weight 🟠")
        else:
            st.error("🔴Obese Please Consult a Doctor Contact on this Number 987654312🔴")


        st.info(""" 
            ***General Score*** 
            1. GuideBelow 18.5: 
            2. Underweight18.5 to 24.9: 
            3. Normal weight25.0 to 29.9: 
            4. Overweight30.0 and above: Obese

        """)    

    else:
        st.error("Height must be greater then 0")


# SideBar
with st.sidebar:
    st.header("About this app")
    st.write("BMI = kg/m²). For imperial units, divide your weight in pounds by height in inches squared and multiply by 703.") 
    st.caption("Body Mass Index is widely used as an indicator of body fat content. Use our BMI calculator for men & women to know your Body Mass Index and determine your ")           

