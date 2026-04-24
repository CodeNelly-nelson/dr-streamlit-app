import streamlit as st

from src.config import APP_TITLE, APP_DESCRIPTION
from src.components.sidebar import render_sidebar
from src.components.header import render_header
from src.components.upload_panel import render_upload_panel
from src.components.results_panel import render_results_panel
from src.services.inference_service import run_demo_inference


def main():
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    render_sidebar()
    render_header(APP_TITLE, APP_DESCRIPTION)

    uploaded_image, run_button = render_upload_panel()

    if uploaded_image is not None and run_button:
        with st.spinner("Analyzing retinal image..."):
            result = run_demo_inference(uploaded_image)

        render_results_panel(result)

    elif uploaded_image is not None:
        st.info("Click **Analyze Image** to run the demo pipeline.")
    else:
        st.warning("Upload a retinal fundus image to begin.")


if __name__ == "__main__":
    main()
