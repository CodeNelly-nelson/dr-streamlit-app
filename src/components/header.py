import streamlit as st


def render_header(title: str, description: str):
    st.title(title)
    st.write(description)

    st.markdown(
        """
        <div style="padding: 1rem; border-radius: 12px; background-color: #f5f7fa; border: 1px solid #e6e8eb;">
            <strong>Demo Goal:</strong> Upload a fundus image, visualize simulated lesion regions,
            classify DR severity, and explain the model decision flow.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()
