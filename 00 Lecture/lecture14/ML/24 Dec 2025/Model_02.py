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


from sklearn.datasets import load_iris
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['Species'] = iris.target_names[iris.target]
    # rename columns for easier access
    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Species']
    return df

data = load_data()
st.subheader("Iris Dataset")
st.dataframe(data)
    

X = data.drop('Species', axis=1)
y = data['Species']

# train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

@st.cache_resource
def train_model():
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model
model = train_model()
    
# side bar for user input
st.sidebar.subheader("Input Features")
sepal_length = st.sidebar.slider("Sepal Length", 4.0, 8.0, 5.0)  
sepal_width = st.sidebar.slider("Sepal Width", 2.0, 4.5, 3.0)
petal_length = st.sidebar.slider("Petal Length", 1.0, 7.0, 4.0)
petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 1.0)


# create a user input
user_input = pd.DataFrame({
    'sepal_length': [sepal_length],
    'sepal_width': [sepal_width],
    'petal_length': [petal_length],
    'petal_width': [petal_width]
})

st.subheader("User Input Features")
st.write(user_input)
 
# display model performance
st.subheader("Model Performance")
accuracy = model.score(X_test, y_test)
st.write(f"Accuracy: {accuracy*100:.2f}%")

# show prediction
st.subheader("Prediction")
prediction = model.predict_proba(user_input)[0]
proba_df = pd.DataFrame({
    'Species': model.classes_,
    'Probability': prediction
}).sort_values(by='Probability', ascending=False)
st.write(proba_df.set_index('Species'))

