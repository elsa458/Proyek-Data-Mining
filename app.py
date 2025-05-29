import streamlit as st
from pages import 1_Halaman_Utama, 2_Tampilkan_Data, 3_Prediksi_Model

st.set_page_config(page_title="Dashboard Gaya Hidup", layout="wide")

st.title("Dashboard Data Gaya Hidup Mahasiswa dan Stres")
st.markdown("Selamat datang di aplikasi analisis gaya hidup mahasiswa berdasarkan data yang telah dikumpulkan.")

st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih halaman:", ["Halaman Utama", "Tampilkan Data", "Prediksi Model"])

if page == "Halaman Utama":
    1_Halaman_Utama.main()
elif page == "Tampilkan Data":
    2_Tampilkan_Data.main()
elif page == "Prediksi Model":
    3_Prediksi_Model.main()

