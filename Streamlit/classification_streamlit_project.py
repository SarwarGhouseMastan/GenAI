import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
# from seaborn import  load_dataset

def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data , columns=iris.feature_names)
    df["species"] = iris.target
    return df , iris.target_names
df , target_names = load_data()

# df = load_dataset("iris")
# df.head()

# X  , Y = df.iloc[: , :-1] , df["species"]
model = RandomForestClassifier()
model.fit( df.iloc[: , :-1], df["species"])

st.sidebar.title("Input Feature")
sepal_length = st.sidebar.slider("Sepal Length" , float(df["sepal length (cm)"].min()) , float(df["sepal length (cm)"].max()))
sepal_width = st.sidebar.slider("Sepal Width" , float(df["sepal width (cm)"].min()) , float(df["sepal width (cm)"].max()))
petal_length = st.sidebar.slider("Petal Length" , float(df["petal length (cm)"].min()) , float(df["petal length (cm)"].max()))
petal_width = st.sidebar.slider("Petal Width" , float(df["petal width (cm)"].min() ), float(df["petal width (cm)"].max()))

input_data = [[sepal_length , sepal_width , petal_length , petal_width]]


# Prediction

prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

st.write(f"The Predicted species is : {predicted_species}")


