import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("Data Set Student lifestyle.xlsx")

# Judul Dashboard
st.title("Dashboard Data Gaya Hidup Mahasiswa dan Stres")

# Tampilkan tabel data
st.subheader("Data Mahasiswa")
st.dataframe(df)

# Visualisasi contoh
st.subheader("Visualisasi: Jam Belajar vs Tingkat Stres")
fig, ax = plt.subplots()
ax.scatter(df["Study_Hours_Per_Day"], df["Stress_Level"])
ax.set_xlabel("Jam Belajar")
ax.set_ylabel("Tingkat Stres")
st.pyplot(fig)
