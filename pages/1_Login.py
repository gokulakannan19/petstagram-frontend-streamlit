import streamlit as st
from utils.api import post
from utils.auth import save_auth


st.title("Login to Petstagram")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    data = {"email": email, "password": password}
    print(data)
    print("Sending login request...")
    res = post("/auth/login", data=data)
    print(res.status_code)
    if res.status_code == 200:
        token = res.json().get("access_token")
        save_auth(token)
        st.success("Login Successfull!")
        st.switch_page("pages/2_Feed.py")
    else:
        st.error("Login Failed. Invalid Credentials")
