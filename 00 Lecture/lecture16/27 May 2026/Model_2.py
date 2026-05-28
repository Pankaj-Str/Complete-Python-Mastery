import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# page configuration
st.set_page_config(
    page_title="Simple IRIS Predictions App.",
    layout="centered",
    initial_sidebar_state="expanded"
)

# APP TITLE 
st.title("IRIS Flower")
st.markdown(""" 
            Rises are striking, easy-to-grow perennials known for their showy, sword-like foliage and vibrant rainbow of blooms. They feature six distinct petals: three upright "standards" and three drooping "falls". Depending on the variety, they grow from either creeping rhizomes (like Bearded Irises) or bulbs (like Dutch Irises)
            """)

from sklearn.datasets import load_iris

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data,columns=iris.feature_names)
    df['Species'] = iris.target_names[iris.target]
    
    df.columns = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm','Species']
    return df

df = load_data()

X = df.drop('Species',axis=1)
y = df['Species']

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2,random_state=42)

@st.cache_resource
def train_model():
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train,y_train)
    return model
model = train_model()
# Side bar 
st.sidebar.header("Flower Measurements")

SepalLength = st.sidebar.slider("SepalLength (CM) ",4.0,8.0,5.8)
SepalWidth = st.sidebar.slider("SepalWidth (CM) ",2.0,4.5,3.0)
PetalLength = st.sidebar.slider("PetalLength (CM) ",1.0,7.0,4.0)
PetalWidth = st.sidebar.slider("PetalWidth (CM) ",0.1,2.6,1.3)

# create a user input dataframe
user_input = pd.DataFrame(
    {
            'SepalLengthCm':[SepalLength],
            'SepalWidthCm':[SepalWidth],
            'PetalLengthCm':[PetalLength],
            'PetalWidthCm':[PetalWidth]
    }
)
# display 
st.subheader("Your Selected Measurements")
st.write(user_input)
# make predictions 
prediction = model.predict(user_input)[0]
# display predictions 
st.subheader("Model Predictions")
st.success(f"predictions = {prediction.capitalize()}")
st.subheader("predictions Confidence")
prob = model.predict_proba(user_input)[0]
proba_df = pd.DataFrame({
    "Species":model.classes_,
    "probability":prob
}).sort_values("probability",ascending=False)
st.bar_chart(proba_df.set_index("Species"))

with st.expander("View Sample of IRIS Dataset"):
    st.write(df.head(10))
    
st.caption("create by rupali.")

