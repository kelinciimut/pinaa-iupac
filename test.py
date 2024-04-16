import streamlit as st

st.title("Mencari deskripsi unsur ")
kode_unsur = st.text_input("Silahkan masukan kode unsur")
cari = st.button("Mencari deskripsi")

if cari :
        if (kode_unsur =="H"): 
             st.write('Dekripsi nya Helium ')
        elif (kode_unsur =="Li"):
             st.write('Dekripsi nya Litium ')
        elif (kode_unsur =="Fe"): 
             st.write('Dekripsi nya BEEEUSI ')
        else  : 
            st.write('Salah atuh jang kodenya sok tanya tante najla')