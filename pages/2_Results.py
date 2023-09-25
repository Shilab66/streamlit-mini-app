import streamlit as st
import data
import pandas as pd

st.set_page_config(
    # You can also use centered
    layout="wide",
    page_title="Results",
)

st.write("# Results")

df = pd.DataFrame(data.returnData())
st.dataframe(df)