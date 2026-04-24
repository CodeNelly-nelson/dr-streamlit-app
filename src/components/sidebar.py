import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.header("Demo Pipeline")

        st.markdown(
            """
            **Stage 1: Lesion Segmentation**
            - Improved U-Net style workflow
            - Detects lesion-like regions
            - Produces lesion overlay

            **Stage 2: DR Classification**
            - ViT-style classifier
            - Attention-based feature extraction
            - Predicts DR severity stage
            """
        )

        st.divider()

        st.subheader("Model Status")
        st.info(
            "This version is a demo scaffold. Replace the demo service with real trained model files later."
        )

        st.subheader("Safety Note")
        st.warning(
            "This app is for educational/demo use only and is not a medical diagnosis tool."
        )
