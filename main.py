import streamlit as st
from streamlit_option_menu import option_menu

#sidebar
with st.sidebar:
    selected = option_menu('Hitung Luang Bangun',
                           ['Hitung Luang Persegi Panjang',
                            'Hitung Luang Persegi Sama Sisi',
                            'Hitung Luang Segi Tiga'],
                            default_index=0)
#hitung luas persegi panjang
if (selected=='Hitung Luang Persegi Panjang'):
    st.title('Hitung Luang Persegi Panjang')
    panjang = st.number_input("Masukkan Panjang",0)
    lebar = st.number_input("Masukkan Lebar",0)
    hitung = st.button("Hitung Luas")
    if hitung:
        luas = panjang*lebar
        st.success(f"Luas Persegi Panjang Adalah = {luas}")
if (selected=='Hitung Luang Persegi Sama Sisi'):
    st.title('Hitung Luang Persegi Sama Sisi')
    sisi = st.number_input("Masukkan Sisi",0)
    hitung = st.button("Hitung Luas")
    if hitung:
        luas = sisi*sisi
        st.success(f"Luas Persegi Sama Sisi Adalah = {luas}")
if (selected=='Hitung Luang Segi Tiga'):
    st.title('Hitung Luang Segi Tiga')
    alas = st.slider("Masukkan Alas",0,100)
    tinggi = st.slider("Masukkan Tinggi",0,100)
    hitung = st.button("Hitung Luas")
    if hitung:
        luas = 0.5*alas*tinggi
        st.success(f"Luas Segi Tiga Adalah = {luas}")