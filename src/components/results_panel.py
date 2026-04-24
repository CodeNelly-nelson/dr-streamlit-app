import streamlit as st
from src.config import LESION_CLASSES


def render_results_panel(result: dict):
    st.subheader("Analysis Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Predicted DR Stage", result["prediction"])

    with col2:
        st.metric("Confidence", f'{result["confidence"]:.2f}%')

    with col3:
        st.metric("Risk Level", result["risk_level"])

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("Original Image")
        st.image(result["original_image"], use_container_width=True)

    with right:
        st.subheader("Lesion Overlay")
        st.image(result["overlay_image"], use_container_width=True)
        st.caption("Demo overlay: simulated lesion-highlighted regions.")

    st.divider()

    st.subheader("Detected Lesion Summary")

    lesion_cols = st.columns(4)
    for index, (lesion, description) in enumerate(LESION_CLASSES.items()):
        with lesion_cols[index]:
            st.markdown(f"**{lesion}**")
            st.write(description)
            st.metric("Demo Score", f'{result["lesion_scores"][lesion]:.1f}%')

    st.divider()

    st.subheader("Model Explanation")

    st.write(
        """
        The application demonstrates the same high-level logic as the research framework:
        first, suspicious retinal lesion regions are highlighted; then, the enriched image information
        is passed into a classification stage to estimate diabetic retinopathy severity.
        """
    )

    st.markdown("### Pipeline Flow")
    st.code(
        "Fundus Image → Lesion Segmentation → Lesion-Weighted Image → DR Stage Classification → Explainable Output",
        language="text",
    )

    st.download_button(
        label="Download Overlay Image",
        data=result["overlay_bytes"],
        file_name="lesion_overlay_demo.png",
        mime="image/png",
        use_container_width=True,
    )
