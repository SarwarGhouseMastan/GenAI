import pandas as pd
import numpy as np
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

st.title("Welcome Streamlit")

# adding a text box
st.write("This is a text Box")

df = pd.DataFrame({
    "first Column" : [1,2,3,4],
    "Second Column" : [10,20,30,40]
})

# displaying the created Dataframe

st.write(f"This is the created Data Frame")
st.write(df)

# creating a Line chart and displaying 

chart_data = pd.DataFrame(np.random.randn(20 ,3),
                          columns=["a" , "b" , "c"])

st.line_chart(chart_data)


# creating a Input box
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello {name}")


# Slider

age = st.slider("Select your age:" , 0,100,25) # 0 - min , 100 - max , 25 - initial

st.write(f"Your age is {age}")

# Dropdown widget
options = ["Python" , "Java" , "C++" , "Scala"]
choice = st.selectbox("Choose the programming language" , options)

st.write(f"You selected {choice}")

# Upload Button

uploaded_file = st.file_uploader("Choose a CSV file" , type="csv")  # type=["csv" , "json" , "xlsx"]
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)