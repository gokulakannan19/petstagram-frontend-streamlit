import streamlit as st
from utils.api import get
from utils.auth import get_auth, logout

st.title("My Profile")

token = get_auth()
if not token:
    st.error("Please login first")
    st.stop()

headers = {"Authorization": f"Bearer {token}"}
res = get("/user/me", headers=headers)

if res.status_code == 200:
    user = res.json()
    st.write(f"👤 {user['name']}")
    st.write(f"📧 {user['email']}")
else:
    st.error("Failed to load profile")

if st.button("Logout"):
    logout()
    st.switch_page("Home.py")
