import streamlit as st
import requests

st.title("✨ Ghibli-Style Image Generator ✨")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Original Image", use_container_width=True)

    if st.button("Convert to Ghibli Style"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:8000/generate-ghibli/", files=files)

        if response.status_code == 200:
            ghibli_url = response.json()["ghibli_image"]
            st.image(ghibli_url, caption="Ghibli-Style Image", use_container_width=True)
        else:
            st.error("Failed to generate image.")
