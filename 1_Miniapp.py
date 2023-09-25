import streamlit as st
import data

def appendData():
    data.addInfo({"name": name, "fruit": fruit})


st.set_page_config(
    # You can also use centered
    layout="wide",
    page_title="Inputs",
)

st.write("# Inputs")

name = st.text_input("Write your name"),
fruit = st.selectbox("Select a fruit", ("Apple", "Peach", "Banana", "Orange", "Grape", "Strawberry"))

st.button("Submit", on_click=appendData)
