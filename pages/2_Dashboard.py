# pages/2_Dashboard.py
import streamlit as st
from utils.api import get
from utils.auth import get_token, get_user, logout

st.title("Dashboard — My Pets")
token = get_token()
if not token:
    st.error("Please login first.")
    st.stop()

user = get_user()
if not user:
    me = get("/users/me", token=token)
    if me.status_code == 200:
        user = me.json()

st.write(f"Logged in as: **{user.get('username', user.get('email',''))}**")

# Fetch pets
res = get("/pets/", token=token)
if res.status_code != 200:
    st.error("Could not fetch pets: " + res.text)
    st.stop()

pets = res.json()
if not pets:
    st.info("You have no pets yet. Go to Create Pet (Pages → 3_CreatePet).")
else:
    for pet in pets:
        cols = st.columns([1, 4, 2])
        img_col, info_col, action_col = cols
        if pet.get("profile_image_url"):
            img_col.image(pet["profile_image_url"], width=80)
        info_col.markdown(f"**{pet.get('name')}**  \n{pet.get('species','')}, {pet.get('age','')}")
        if action_col.button("View Posts", key=f"view-{pet['id']}"):
            # switch to ViewPosts page and pass pet_id via query param
            st.experimental_set_query_params(pet_id=pet['id'])
            st.experimental_rerun()

st.sidebar.button("Logout", on_click=lambda: (logout(), st.experimental_rerun()))
