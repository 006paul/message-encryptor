# Ciphry

A small Streamlit web app for experimenting with ROT13 and Caesar cipher encryption and decryption.

## Live demo

[Open Ciphry](https://ciphry.streamlit.app/)

## Features

- ROT13 cipher with a fixed shift of 13
- Caesar cipher with a selectable shift from 1 to 25
- Encrypt and decrypt modes
- Live text conversion as you type

## Requirements

- Python 3.11 or later
- `pip`

## Local setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Start the app with:

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## Dev Container

The repository includes a `.devcontainer/devcontainer.json` configuration for VS Code Dev Containers or GitHub Codespaces. It installs the Python dependencies and starts the Streamlit app on port `8501`.

## Note

These ciphers are intended for learning and experimentation. They should not be used to protect sensitive information.

## Previous versions

Earlier releases included a Tkinter desktop application. The current version is the Streamlit web app available above.
