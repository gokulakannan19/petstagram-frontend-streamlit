# pages/5_ViewPosts.py
import streamlit as st
from utils.api import get, post, delete
from utils.auth import get_token
from datetime import datetime

st.title("View Posts")

token = get_token()
if not token:
    st.error("Please login first.")
    st.stop()

# get selected pet_id from query params
params = st.experimental_get_query_params()
pet_id = params.get("pet_id", [None])[0]

if not pet_id:
    st.info("Select a pet from Dashboard to view posts.")
    st.stop()

# fetch posts for pet (endpoint: GET /api/v1/posts/{pet_id})
res = get(f"/posts/{pet_id}", token=token)
if res.status_code != 200:
    st.error("Failed to load posts: " + res.text)
    st.stop()

posts = res.json()
if not posts:
    st.info("No posts for this pet yet.")
else:
    for p in posts:
        st.markdown(f"**{p.get('caption','')}**")
        if p.get("image_url"):
            st.image(p["image_url"], use_column_width=True)
        st.write(f"Posted at: {p.get('created_at','')}")
        cols = st.columns([1,1,1,6])
        like_col, comm_col, del_col, spacer = cols
        if like_col.button("Like ❤️", key=f"like-{p['id']}"):
            resp = post(f"/likes/{p['id']}", token=token)
            if resp.status_code in (200,201):
                st.success("Liked")
                st.experimental_rerun()
            else:
                st.error("Like failed: " + resp.text)
        if comm_col.button("Comments", key=f"comm-{p['id']}"):
            st.experimental_set_query_params(pet_id=pet_id, post_id=p['id'])
            st.experimental_rerun()
        if del_col.button("Delete", key=f"del-{p['id']}"):
            d = delete(f"/posts/{p['id']}", token=token)
            if d.status_code in (200,204):
                st.success("Deleted")
                st.experimental_rerun()
            else:
                st.error("Delete failed: " + d.text)
        st.divider()
