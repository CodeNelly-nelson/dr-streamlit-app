import streamlit as st
from PIL import Image


def render_upload_panel():
    st.subheader("Upload Retinal Fundus Image")

    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png"],
        help="Upload a retinal fundus image for the demo.",
    )

    uploaded_image = None

    if uploaded_file is not None:
        uploaded_image = Image.open(uploaded_file).convert("RGB")

        col1, col2 = st.columns([1, 1])

        with col1:
            st.image(uploaded_image, caption="Uploaded Fundus Image", use_container_width=True)

        with col2:
            st.markdown("### Image Details")
            st.write(f"**File name:** {uploaded_file.name}")
            st.write(f"**Image size:** {uploaded_image.size[0]} × {uploaded_image.size[1]} pixels")
            st.write(f"**Mode:** {uploaded_image.mode}")

    run_button = st.button("Analyze Image", type="primary", use_container_width=True)

    st.divider()

    return uploaded_image, run_button
