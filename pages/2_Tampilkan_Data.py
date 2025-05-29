import streamlit as st
import pandas as pd

st.title("Tampilkan Data Mahasiswa")

# Load data
df = pd.read_excel("Data Set Student lifestyle.xlsx")

# Tampilkan dataframe
st.dataframe(df)
