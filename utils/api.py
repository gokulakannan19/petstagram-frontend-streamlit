import requests
from config import BACKEND_URL


def post(path, data=None, files=None, headers=None):
    url = f"{BACKEND_URL}/api/v1/{path}"
    response = requests.post(url, data=data, files=files, headers=headers)
    return response


def get(path, headers=None):
    url = f"{BACKEND_URL}/api/v1/{path}"
    response = requests.get(url, headers=headers)
    return response


