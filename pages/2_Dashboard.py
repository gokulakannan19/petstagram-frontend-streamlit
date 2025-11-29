# pages/2_Feed.py
import streamlit as st
from utils.api import get, post
from utils.auth import get_token, get_user, logout
from datetime import datetime

st.title("Feed")
token = get_token()
if not token:
    st.error("Please login first.")
    st.stop()

# fetch feed from backend - implement a /posts/feed or /posts endpoint returning combined data
res = get("/posts/feed", token=token)
if res.status_code != 200:
    st.error("Failed to load feed: " + res.text)
    st.stop()

posts = res.json()  # expected list of posts with keys: id, pet (or pet_name), caption, image_url, like_count, comment_count, liked_by_user
for post in posts:
    st.markdown(f"**{post.get('pet_name', 'Pet')}** • `{post.get('created_at', '')}`")
    if post.get("image_url"):
        st.image(post["image_url"], use_column_width=True)
    st.write(post.get("caption", ""))
    col1, col2, col3 = st.columns([1,1,6])
    with col1:
        if st.button(f"Like ❤️ {post.get('like_count',0)}", key=f"like-{post['id']}"):
            r = post  # avoid shadowing
            resp = post  # placeholder
    with col2:
        if st.button(f"Comments 💬 {post.get('comment_count',0)}", key=f"c-{post['id']}"):
            # show comments in expander
            comments_res = get(f"/posts/{post['id']}/comments", token=token)
            if comments_res.status_code == 200:
                comments = comments_res.json()
                for c in comments:
                    st.write(f"**{c['user_id']}**: {c['text']}")
            else:
                st.error("Could not load comments")
    with col3:
        st.write("")  # space

st.sidebar.button("Logout", on_click=lambda: (logout(), st.experimental_rerun()))
