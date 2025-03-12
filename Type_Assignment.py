import streamlit as st
import pandas as pd

st.title("Type Assignment")

@st.cache_data
def load_data():
    df = pd.read_csv("data/type.csv")
    df["confidence(%)"] = df["confidence(%)"].round(2)
    df.index = df.index + 1
    return df

df = load_data()
st.write(df)