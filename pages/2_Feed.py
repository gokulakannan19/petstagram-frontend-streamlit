import streamlit as st
from utils.api import get
from utils.auth import get_auth, logout


st.title("Pet Feed")

token = get_auth()

if not token:
    st.error("You must be logged in to view the feed. Please login first")
    st.stop()

headers = {"Authorization": f"Bearer {token}"}
res = get("/posts/feed", headers=headers)

if res.status_code == 200:
    posts = res.json()

    for post in posts:
        st.image(post["image_url"])
        st.write(f"🐶 Pet: {post['pet_name']}")
        st.write(post["caption"])
        st.divider()
else:
    st.error("Error loading feed")