import streamlit as st
from utils.api import post
from utils.auth import get_auth


st.title("Upload a Pet photo")

token = get_auth()
if not token:
    st.error("You must be logged in to upload a photo. Please login first")
    st.stop()

caption = st.text_input("Caption")
file = st.file_uploader("Upload your pet photo", type=["png", "jpg", "jpeg"])

if st.button("Upload"):
    if file:
        files = {"file": file}
        data = {"caption": caption}
        headers = {"Authorization": f"Bearer {token}"}

        res = post("/posts/upload", data=data, files=files, headers=headers)

        if res.status_code == 200:
            st.success("Posted Successfully!")
        else:
            st.error("Upload Failed")

