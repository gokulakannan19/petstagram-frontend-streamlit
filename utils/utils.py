import streamlit as st


def save_auth(token: str) -> None:
    st.session_state["token"] = token


def get_auth() -> str | None:
    return st.session_state.get("token")


def logout() -> None:
    st.session_state.clear()