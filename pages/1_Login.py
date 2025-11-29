# pages/1_Login.py
import streamlit as st
from utils.api import post, get
from utils.auth import save_token, save_user, get_token
from config import BACKEND_URL

st.title("Login / Register")

mode = st.radio("Mode", ["Login", "Register"])

if mode == "Login":
    st.subheader("Login")
    username = st.text_input("Username or Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # many backends expect form or JSON; adjust if your backend uses OAuth2PasswordRequestForm
        res = post("/auth/login", data={"username": username, "password": password})
        if res.status_code == 200:
            token = res.json().get("access_token")
            save_token(token)
            # fetch profile
            user_res = get("/users/me", token=token)
            if user_res.status_code == 200:
                save_user(user_res.json())
            st.success("Logged in — go to Feed")
            # Ensure session_state key for rerun is initialized
            if "rerun" not in st.session_state:
                st.session_state["rerun"] = False
            st.session_state["rerun"] = True
            st.stop()
        else:
            st.error("Login failed: " + res.text)

else:
    st.subheader("Register")
    username = st.text_input("Username", key="reg_user")
    email = st.text_input("Email", key="reg_email")
    password = st.text_input("Password", type="password", key="reg_pass")
    if st.button("Register"):
        res = post("/users/", json={"username": username, "email": email, "password": password})
        if res.status_code in (200, 201):
            st.success("Registered. Please login.")
        else:
            st.error("Register failed: " + res.text)
