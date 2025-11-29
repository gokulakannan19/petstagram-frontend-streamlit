# pages/3_CreatePet.py
import streamlit as st
from utils.api import post
from utils.auth import get_token

st.title("Create Pet")
token = get_token()
if not token:
    st.error("Please login first.")
    st.stop()

name = st.text_input("Pet name")
species = st.text_input("Species (e.g., dog, cat)")
breed = st.text_input("Breed (optional)")
age = st.number_input("Age", min_value=0, max_value=80, value=1)
bio = st.text_area("Short bio (optional)")

profile_img = st.file_uploader("Profile image (optional)", type=["jpg","jpeg","png"])

if st.button("Create Pet"):
    payload = {"name": name, "species": species, "breed": breed or None, "age": int(age), "bio": bio or None}
    # create pet first
    res = post("/pets/", token=token, json=payload)
    if res.status_code in (200,201):
        pet = res.json()
        st.success("Pet created")
        pet_id = pet.get("id")
        if profile_img and pet_id:
            # upload profile image
            from io import BytesIO
            file_bytes = profile_img.read()
            files = {"file": (profile_img.name, BytesIO(file_bytes), profile_img.type)}
            up = post(f"/api/v1/pets/{pet_id}/upload-image", token=token, files=files)
            if up.status_code == 200:
                st.success("Profile image uploaded")
            else:
                st.error("Profile image upload failed: " + up.text)
    else:
        st.error("Create pet failed: " + res.text)
