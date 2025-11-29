import requests
from typing import Optional
from config import BACKEND_URL


def _url(path: str) -> str:
    if path.startswith("/"):
        path = path[1:]
    return f"{BACKEND_URL}/api/v1/{path}"


def get(path: str, token: Optional[str] = None, params: dict|None = None):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return requests.get(_url(path), headers=headers, params=params, timeout=15)


def post(path: str, token: Optional[str] = None, json: dict | None = None, data: dict | None = None, files: dict | None = None):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return requests.post(_url(path), headers=headers, json=json, data=data, files=files, timeout=15)


def put(path: str, token: Optional[str] = None, json: dict | None = None):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return requests.put(_url(path), headers=headers, json=json, timeout=15)


def delete(path: str, token: Optional[str] = None):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return requests.delete(_url(path), headers=headers, timeout=15)
