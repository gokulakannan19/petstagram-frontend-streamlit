# petstagram-frontend-streamlit
## Overview

Streamlit frontend for the Petstagram backend. Lightweight UI to browse pets and posts, authenticate, create pets/posts and upload images. Configurable backend URL so it can point to a local or remote API.

## Features

- Login / logout
- Browse pets and pet profiles
- View and create photo posts
- Upload images for pets/posts
- Like and comment on posts (UI hooks; behavior depends on backend)

## Requirements

- Python 3.9+
- pip
- Streamlit

## Installation

1. Create virtual environment and install dependencies:
    - python -m venv .venv
    - source .venv/bin/activate  (Windows: .venv\Scripts\activate)
    - pip install -r requirements.txt

2. (Optional) Install dev tools:
    - pip install black isort flake8

## Configuration

The frontend needs the backend base URL. Provide it via an environment variable or a small config file.

Example with environment variable:
- export PETSTAGRAM_BACKEND_URL="http://localhost:8000"
- On Windows (PowerShell): $env:PETSTAGRAM_BACKEND_URL="http://localhost:8000"

Example .env:
PETSTAGRAM_BACKEND_URL=http://localhost:8000

Adjust the variable name in the app if your code expects a different key.

## Run

Start the Streamlit app:
- streamlit run app.py

If your main script is under src/ use:
- streamlit run src/app.py

Open the URL printed by Streamlit (usually http://localhost:8501).

## Backend endpoints (expected)

The frontend expects a REST API with endpoints similar to:
- POST /api/auth/login
- POST /api/auth/register
- GET  /api/pets
- GET  /api/pets/{id}
- POST /api/pets
- GET  /api/posts
- GET  /api/posts/{id}
- POST /api/posts
- POST /api/uploads

Adjust requests in the frontend if your backend uses different paths or auth flows.

## Deployment

- Containerize with a small Dockerfile that installs dependencies and runs `streamlit run`.
- Ensure PETSTAGRAM_BACKEND_URL is set in the environment of your deployment target.

## Contributing

- Fork, create a branch, submit PR.
- Follow coding style and add tests for new logic where applicable.

## License

Specify the project license (e.g., MIT) in LICENSE file.

