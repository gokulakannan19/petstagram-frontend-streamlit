# utils/auth.py
import streamlit as st

TOKEN_KEY = "auth_token"
USER_KEY = "current_user"


def save_token(token: str):
    st.session_state[TOKEN_KEY] = token


def get_token() -> str | None:
    return st.session_state.get(TOKEN_KEY)


def save_user(user: dict):
    st.session_state[USER_KEY] = user


def get_user() -> dict | None:
    return st.session_state.get(USER_KEY)


def logout():
    for k in [TOKEN_KEY, USER_KEY]:
        if k in st.session_state:
            del st.session_state[k]
