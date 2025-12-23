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
    