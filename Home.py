import streamlit as st

st.title("🐾 Petstagram")
st.write("Welcome to the MVP version of Petstagram!")

if st.button("Go to Login"):
    st.switch_page("pages/1_Login.py")
