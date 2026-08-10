import streamlit as st
import pandas as pd
import numpy as np
# pip install scikit-learn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score , classification_report
import pickle
# pip install plotly
import plotly.express as px
import os

# run files 
# pip install streamlit
# streamlit run Model_example01.py

# page config 
st.set_page_config(
    page_title="IRIS ML CLASSIFICATION",
    page_icon="🥳",
    layout="centered"
)

st.title("IRIS Flower Species Classifier")
st.write("Train a Machine Learning Model")

# side bar
st.sidebar.header("Model Settings")

# options - train a new model 
train_new = st.sidebar.checkbox("Train a new Model ",value=True)

@st.cache_resource
def load_and_train_model():
    #load data
    iris = load_iris()
    X = pd.DataFrame(iris.data , columns=iris.feature_names)
    y = iris.target
    target_names = iris.target_names
    # split data
    X_train , X_test , y_train ,y_test = train_test_split(X, y , test_size=0.2,random_state=42)

    # train random forest model
    model = RandomForestClassifier(n_estimators=100,random_state=42)
    model.fit(X_train,y_train)

    # evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test,y_pred)
    return model , X , y , target_names , accuracy , X_train.columns.tolist()

if train_new or not os.path.exists("iris_model.pkl"):
    model , X , y , target_names , accuracy , feature_names = load_and_train_model()
    # save model
    with open("iris_model.pkl","wb") as f:
        pickle.dump((model,target_names,feature_names), f)
    st.sidebar.success(f"Model Trained ! Accuracy : {accuracy:.2%}")
else:
    with open("iris_model.pkl","wb") as f:
            model , target_names , feature_names = pickle.load(f)
    st.sidebar.success("Loaded Pre-Trained Model")    

# Main input 
st.subheader("Enter Flower Measurements")
col1 , col2 = st.columns(2)
with col1:
     sepal_length = st.slider("SepalLengthCm",4.0,8.0,5.5,0.1)
     Sepal_Width = st.slider("SepalWidthCm",2.0,4.5,3.0,0.1)

with col1:
     Petal_Length = st.slider("PetalLengthCm",1.0,7.0,4.0,0.1)
     Petal_Width = st.slider("PetalWidthCm",0.1,2.5,1.3,0.1)


# Create a input dataframe for prediction
input_data = pd.DataFrame({
     feature_names[0] :[sepal_length],
     feature_names[1] :[Sepal_Width],
     feature_names[2] :[Petal_Length],
     feature_names[3] :[Petal_Width]
})
# predict button 
if st.button("Predict Species",type="primary",use_container_width=True):
     prediction = model.predict(input_data)[0]
     prediction_proba = model.predict_proba(input_data)[0]

     predicted_species = target_names[prediction]

     st.success(f"Predicted Species : {predicted_species}")

     # show probabilities
     st.write("Predictions Probabilities")
     prob_df = pd.DataFrame({
          "Species": target_names,
          "Probability":prediction_proba
     })
     st.bar_chart(prob_df.set_index("Species"))

# model Performance Section 
st.subheader("Model Performance")

if 'accuracy' in locals():
     st.metric("Test Accuracy ",f"{accuracy:.2%}")

if st.checkbox("Show DataSet"):
     st.write("### IRIS DATASET PREVIEW")
     iris_df = pd.DataFrame(X)
     iris_df['species'] = pd.Series(y).map({0:'setosa',1:'versicolor',2:'virginica'})
     st.dataframe(iris_df.head())

     # scatter
     fig = px.scatter(
          iris_df,
          x="sepal length (cm)",
          y="petal length (cm)",
          color="species",
          title="Sepal width vs patal length",
          hover_data=["sepal length (cm)","petal length (cm)"]
     )
     st.plotly_chart(fig,use_container_width=True)