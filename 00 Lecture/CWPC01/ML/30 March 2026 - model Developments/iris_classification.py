import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
# import plotly.express as px
import pickle
import os
import matplotlib.pyplot as plt


# page configuration
st.set_page_config(
    page_title="Iris Classification",
    page_icon="🌸",
    layout="centered")

st.title("Iris Classification with Random Forest")
st.write("This app classifies iris flowers based on their features using a Random Forest Classifier.")

# side bar 
st.sidebar.header("Model Settings")

# option load 
train_new = st.sidebar.checkbox("Train New Model", value=True)

@st.cache_data

def load_and_train_model():
    # load data 
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target
    
    target_names = iris.target_names
    
    # splits data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # train model random forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # evaluate model
    y_test_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_test_pred)
    
    return model, target_names, accuracy , X_train.columns.tolist()


if train_new or not os.path.exists("iris_rf_model.pkl"):
    model, target_names, accuracy, feature_names = load_and_train_model()
    # save model
    with open("iris_rf_model.pkl", "wb") as f:
        pickle.dump((model,target_names,feature_names),f)
    st.sidebar.success(f"Model trained with accuracy: {accuracy:.2f}")
else:
    with open("iris_rf_model.pkl", "rb") as f:
        model, target_names, feature_names = pickle.load(f)
    st.sidebar.info("Loaded existing model")
    
# main input form
st.subheader("Enter Flower Measurements")

col1 , col2 = st.columns(2)
with col1:
    sepal_length = st.slider("Sepal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
    sepal_width = st.slider("Sepal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)
with col2:    
    petal_length = st.slider("Petal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
    petal_width = st.slider("Petal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)
    
# create input data frame
input_data = pd.DataFrame(
    {
        feature_names[0]: [sepal_length],
        feature_names[1]: [sepal_width],
        feature_names[2]: [petal_length],
        feature_names[3]: [petal_width]
    }
)

# predict button
if st.button("Predict",type="primary" , use_container_width=True):
    prediction = model.predict(input_data)[0]
    predicted_class = target_names[prediction]
    st.success(f"The predicted iris species is: {predicted_class}")
    
    # show probability
    st.write("Prediction Probabilities:")
    prob_df = pd.DataFrame({
        "Species": target_names,
        "Probability": model.predict_proba(input_data)[0]
    })
    st.bar_chart(prob_df.set_index("Species"))


# model performance
st.subheader("Model Performance")
if 'accuracy' in locals():
    st.write(f"Model Accuracy: {accuracy:.2f}")
else:
    st.write("Model accuracy not available. Please train a new model to see performance metrics.")

# option show database preview
if st.checkbox("Show Iris Dataset Preview"):
    st.write("The Iris dataset contains measurements of iris flowers and their corresponding species.")
    iris_df = pd.DataFrame(load_iris().data, columns=feature_names)
    iris_df["species"] = pd.Series(load_iris().target).map({0 : "setosa", 1 : "versicolor", 2 : "virginica"})
    st.dataframe(iris_df.head())
    
    # scatter plot
    st.subheader("Scatter Plot of Iris Dataset")
    fig =   plt.figure(figsize=(10,6))
    for species in target_names:
        subset = iris_df[iris_df["species"] == species]
        plt.scatter(subset[feature_names[0]], subset[feature_names[2]], label=species)
    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[2])
    plt.title("Sepal Length vs Petal Length")
    plt.legend()
    st.pyplot(fig)
    plt.close()  
    

# footer 
st.caption("This app was developed for educational purposes using Streamlit and Scikit-learn.")    