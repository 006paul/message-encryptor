import streamlit as st
from st_keyup import st_keyup

st.set_page_config(page_title="Ciphry", layout="wide")

if "mode" not in st.session_state:
    st.session_state["mode"] = "Encrypt"
if "input" not in st.session_state:
    st.session_state["input"] = 0

def toggle_mode():
    if st.session_state["mode"] == "Encrypt":
        st.session_state["mode"] = "Decrypt"
    else:
        st.session_state["mode"] = "Encrypt"
    st.session_state["input"] += 1

def cipher_option(cipher, text, key):
    if st.session_state["mode"] == "Encrypt":
        if cipher == "caesar":
            return caesar_encryption(text, key)
        elif cipher == "rot13":
            return rot13_cipher_encryption(text)
    else:
        if cipher == "caesar":
            return caesar_decryption(text, key)
        elif cipher == "rot13":
            return rot13_cipher_decryption(text)
        
def caesar_encryption(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decryption(text, key):
    return caesar_encryption(text, -key)

def rot13_cipher_encryption(text):
    return caesar_encryption(text, key=13)

def rot13_cipher_decryption(text):
    return caesar_decryption(text, key=13)

st.title("Cryptography tool")

with st.container():
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        cipher_labels = {"rot13" : "ROT13 Cipher",
                        "caesar" : "Caesar Cipher (custom key shift)"}
        cipher_options = ["rot13", "caesar"]
        selected_cipher = st.selectbox("Select cipher algorithm", options=cipher_options, format_func=lambda code: cipher_labels.get(code, code),
                                    help="The Caesar Cipher requires a shift key. ROT13 automatically shifts by 13")

    with col2:
        if selected_cipher == "caesar":
            shift_key = st.slider("Select shift key", min_value=1, max_value=25, value=4, key="shift")
        else:
            shift_key = 13

    with col3:
        st.write(f"Current mode: {st.session_state['mode']}ing")
        st.button(f"Switch to {'Decrypt' if st.session_state['mode'] == 'Encrypt' else 'Encrypt'}", on_click=toggle_mode, use_container_width=True)

st.divider()

work_col1, work_col2 = st.columns(2)

action_word = "encrypt" if st.session_state["mode"] == "Encrypt" else "decrypt"

with work_col1:
    st.subheader("Plaintext" if st.session_state["mode"] == "Encrypt" else "Ciphertext")
    user_text = st_keyup(f"", placeholder="Type here...", key=st.session_state["input"], label_visibility="collapsed")

with work_col2:
    st.subheader(f"{st.session_state['mode']}ed text:")
    result = cipher_option(selected_cipher, user_text, shift_key)
    st.text_input(
        label="hidden_output",
        value=result,
        placeholder="Waiting for input...",
        disabled=True,
        label_visibility="collapsed"
    )