# pages/6_Comments.py
import streamlit as st
from utils.api import get, post, delete
from utils.auth import get_token

st.title("Comments")

token = get_token()
if not token:
    st.error("Please login first.")
    st.stop()

params = st.experimental_get_query_params()
post_id = params.get("post_id", [None])[0]
pet_id = params.get("pet_id", [None])[0]

if not post_id:
    st.info("Open a post's Comments from View Posts page.")
    st.stop()

# list comments
res = get(f"/comments/{post_id}", token=token)
if res.status_code == 200:
    comments = res.json()
    for c in comments:
        st.markdown(f"**User {c.get('user_id')}** • {c.get('created_at','')}")
        st.write(c.get("text"))
        if st.button("Delete", key=f"delc-{c['id']}"):
            d = delete(f"/comments/{c['id']}", token=token)
            if d.status_code in (200,204):
                st.success("Deleted")
                st.experimental_rerun()
            else:
                st.error("Delete failed: " + d.text)
        st.divider()
else:
    st.error("Could not load comments: " + res.text)

# add comment
text = st.text_area("New comment")
if st.button("Add comment"):
    if not text.strip():
        st.error("Write something first")
    else:
        r = post(f"/comments/{post_id}", token=token, json={"text": text})
        if r.status_code in (200,201):
            st.success("Comment added")
            st.experimental_rerun()
        else:
            st.error("Add comment failed: " + r.text)
