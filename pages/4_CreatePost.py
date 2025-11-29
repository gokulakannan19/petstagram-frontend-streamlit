# pages/4_CreatePost.py
import streamlit as st
from utils.api import get, post
from utils.auth import get_token
from io import BytesIO

st.title("Create Post")
token = get_token()
if not token:
    st.error("Please login first.")
    st.stop()

# fetch pets
pets_res = get("/pets/", token=token)
if pets_res.status_code != 200:
    st.error("Cannot fetch pets: " + pets_res.text)
    st.stop()

pets = pets_res.json()
if not pets:
    st.info("You have no pets yet. Create one first.")
    st.stop()

pet_map = {f"{p['name']} (id:{p['id']})": p['id'] for p in pets}
sel = st.selectbox("Choose pet", options=list(pet_map.keys()))
pet_id = pet_map[sel]

caption = st.text_area("Caption (optional)")
img = st.file_uploader("Post image", type=["jpg","jpeg","png"])

if st.button("Upload Image and Create Post"):
    if not img:
        st.error("Please choose an image")
    else:
        file_bytes = img.read()
        files = {"file": (img.name, BytesIO(file_bytes), img.type)}
        up = post(f"/posts/{pet_id}/upload-image", token=token, files=files)
        if up.status_code == 200:
            image_url = up.json().get("image_url")
            # create post
            create_res = post("/posts/", token=token, json={"pet_id": pet_id, "caption": caption, "image_url": image_url})
            if create_res.status_code in (200,201):
                st.success("Post created")
            else:
                st.error("Create post failed: " + create_res.text)
        else:
            st.error("Upload failed: " + up.text)
