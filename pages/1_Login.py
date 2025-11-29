# pages/1_Login.py
import streamlit as st
from utils.api import post, get
from utils.auth import save_token, save_user, get_token
from config import BACKEND_URL

st.title("Login / Register")

mode = st.radio("Mode", ["Login", "Register"])

if mode == "Login":
    st.subheader("Login")
    username = st.text_input("Username or Email", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login"):
        # Many FastAPI auth endpoints expect form data (OAuth2). We'll try form data.
        res = post("/auth/login", data={"username": username, "password": password})
        if res.status_code == 200:
            body = res.json()
            token = body.get("access_token") or body.get("token") or body.get("accessToken")
            if not token:
                st.error("Login succeeded but token not found in response.")
            else:
                save_token(token)
                # fetch user profile
                me = get("/users/me", token=token)
                if me.status_code == 200:
                    save_user(me.json())
                st.success("Logged in. Go to Dashboard (Pages → 2_Dashboard).")
                if "rerun" not in st.session_state:
                    st.session_state["rerun"] = False

                # Trigger rerun logic
                st.session_state["rerun"] = True
                st.stop()  # Stops execution, and Streamlit will rerun the script
        else:
            st.error(f"Login failed: {res.status_code} {res.text}")

else:
    st.subheader("Register")
    username = st.text_input("Username", key="reg_user")
    email = st.text_input("Email", key="reg_email")
    password = st.text_input("Password", type="password", key="reg_pass")

    if st.button("Register"):
        res = post("/users/", json={"username": username, "email": email, "password": password})
        if res.status_code in (200, 201):
            st.success("Registered successfully. Please login.")
        else:
            st.error(f"Registration failed: {res.status_code} {res.text}")
