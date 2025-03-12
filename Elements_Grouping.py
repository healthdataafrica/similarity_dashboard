import streamlit as st
import pandas as pd

st.title("Elements Grouping")

@st.cache_data
def load_data():
    df = pd.read_csv("data/grouping.csv")
    df.index = df.index + 1
    df["number of members"] = df["members"].astype(str).apply(lambda x: len(x.split(",")) if x.strip() else 0)
    return df

df = load_data()
st.write(df)