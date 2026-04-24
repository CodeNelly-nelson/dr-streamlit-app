import time
import random
from io import BytesIO

import numpy as np
import streamlit as st
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Diabetic Retinopathy AI Demo",
    page_icon="🩺",
    layout="wide",
)


# -----------------------------
# Helper functions
# -----------------------------
def resize_image(image: Image.Image, max_size=(700, 700)) -> Image.Image:
    image = image.convert("RGB")
    image.thumbnail(max_size)
    return image


def create_demo_lesion_overlay(image: Image.Image):
    """
    Creates a simulated lesion segmentation overlay for demo purposes.
    This is NOT a medical diagnosis model. Replace this function with your trained U-Net output later.
    """
    image = image.convert("RGB")
    w, h = image.size

    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    rng = random.Random(w * h)

    lesion_types = {
        "Microaneurysms (MA)": {"color": (0, 102, 255, 155), "count": rng.randint(8, 18), "radius": (3, 8)},
        "Hemorrhages (HE)": {"color": (255, 0, 0, 135), "count": rng.randint(4, 9), "radius": (8, 22)},
        "Hard Exudates (EX)": {"color": (255, 215, 0, 150), "count": rng.randint(4, 10), "radius": (6, 16)},
        "Soft Exudates (SE)": {"color": (0, 190, 90, 145), "count": rng.randint(2, 6), "radius": (10, 24)},
    }

    counts = {}
    center_x, center_y = w // 2, h // 2

    for lesion_name, cfg in lesion_types.items():
        counts[lesion_name] = cfg["count"]
        for _ in range(cfg["count"]):
            # Bias points toward retinal center so it looks more realistic
            x = int(rng.gauss(center_x, w / 5))
            y = int(rng.gauss(center_y, h / 5))
            x = max(10, min(w - 10, x))
            y = max(10, min(h - 10, y))
            r = rng.randint(*cfg["radius"])
            draw.ellipse((x - r, y - r, x + r, y + r), fill=cfg["color"])

    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=0.7))
    blended = Image.alpha_composite(image.convert("RGBA"), overlay)
    return blended.convert("RGB"), counts


def classify_demo(counts):
    """
    Rule-based demo classifier.
    Replace this with your ViT-CBAM/GCN model inference later.
    """
    total_lesions = sum(counts.values())
    he = counts.get("Hemorrhages (HE)", 0)
    ex = counts.get("Hard Exudates (EX)", 0)
    ma = counts.get("Microaneurysms (MA)", 0)
    se = counts.get("Soft Exudates (SE)", 0)

    severity_score = total_lesions + (he * 1.7) + (ex * 1.4) + (se * 1.2) + (ma * 0.6)

    if severity_score < 18:
        stage = "Mild DR"
        confidence = random.uniform(88, 92)
        risk = "Low to moderate"
    elif severity_score < 34:
        stage = "Moderate DR"
        confidence = random.uniform(92, 96)
        risk = "Moderate"
    elif severity_score < 48:
        stage = "Severe DR"
        confidence = random.uniform(94, 97.5)
        risk = "High"
    else:
        stage = "Proliferative DR"
        confidence = random.uniform(95, 98.7)
        risk = "Very high"

    return stage, confidence, risk, severity_score


def image_to_download_bytes(image: Image.Image):
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("🩺 DR AI Demo")
    st.caption("Portfolio-ready Streamlit demo")

    st.markdown("### Pipeline")
    st.write("1. Upload fundus image")
    st.write("2. Simulate lesion segmentation")
    st.write("3. Generate lesion-weighted overlay")
    st.write("4. Predict DR severity stage")
    st.write("5. Explain model decision")

    st.markdown("---")
    st.markdown("### Lesion Legend")
    st.markdown("🔵 Microaneurysms (MA)")
    st.markdown("🔴 Hemorrhages (HE)")
    st.markdown("🟡 Hard Exudates (EX)")
    st.markdown("🟢 Soft Exudates (SE)")

    st.markdown("---")
    st.warning(
        "Demo only. This app is not a medical device and should not be used for diagnosis."
    )


# -----------------------------
# Header
# -----------------------------
st.title("Diabetic Retinopathy Detection & Stage Classification")
st.write(
    "A Streamlit demo of a two-stage AI pipeline: lesion segmentation followed by diabetic retinopathy stage classification."
)

st.info(
    "This version uses simulated segmentation and rule-based classification for demonstration. Later, you can replace these parts with your trained U-Net and ViT-CBAM/GCN models."
)


# -----------------------------
# Upload section
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload a retinal fundus image",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is None:
    st.markdown("### What this demo will show")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("1. Segmentation")
        st.write("Detects lesion-like regions in retinal images.")

    with col2:
        st.subheader("2. Classification")
        st.write("Predicts DR stage: Mild, Moderate, Severe, or Proliferative.")

    with col3:
        st.subheader("3. Explainability")
        st.write("Shows which lesion types influenced the prediction.")

    st.stop()


# -----------------------------
# Processing
# -----------------------------
input_image = Image.open(uploaded_file)
input_image = resize_image(input_image)

with st.spinner("Analyzing retinal image..."):
    time.sleep(1.2)
    overlay_image, lesion_counts = create_demo_lesion_overlay(input_image)
    stage, confidence, risk, severity_score = classify_demo(lesion_counts)


# -----------------------------
# Results display
# -----------------------------
st.markdown("## Analysis Results")

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
with metric_col1:
    st.metric("Predicted Stage", stage)
with metric_col2:
    st.metric("Confidence", f"{confidence:.2f}%")
with metric_col3:
    st.metric("Risk Level", risk)
with metric_col4:
    st.metric("Lesion Score", f"{severity_score:.1f}")

st.markdown("---")

img_col1, img_col2 = st.columns(2)

with img_col1:
    st.subheader("Original Fundus Image")
    st.image(input_image, use_container_width=True)

with img_col2:
    st.subheader("Lesion-Weighted Overlay")
    st.image(overlay_image, use_container_width=True)
    st.download_button(
        label="Download Overlay Image",
        data=image_to_download_bytes(overlay_image),
        file_name="lesion_overlay.png",
        mime="image/png",
    )

st.markdown("---")


# -----------------------------
# Lesion statistics
# -----------------------------
st.markdown("## Detected Lesion Summary")

lesion_cols = st.columns(4)
lesion_items = list(lesion_counts.items())
for col, (lesion_name, count) in zip(lesion_cols, lesion_items):
    with col:
        st.metric(lesion_name, count)

st.markdown("---")


# -----------------------------
# Explanation
# -----------------------------
st.markdown("## Model Explanation")

st.write(
    f"The demo detected a total of **{sum(lesion_counts.values())} lesion-like regions**. "
    f"The strongest contributors to the final prediction were hemorrhages, exudates, and total lesion density. "
    f"Based on this lesion pattern, the system predicted **{stage}** with **{confidence:.2f}% confidence**."
)

with st.expander("How the real research pipeline works"):
    st.markdown(
        """
        **Stage 1: Lesion Segmentation**  
        A U-Net-based model identifies lesion regions such as microaneurysms, hemorrhages, hard exudates, and soft exudates.

        **Stage 2: Lesion-Aware Classification**  
        The segmented lesion information is converted into lesion-weighted inputs and passed into a Vision Transformer-based classifier.

        **Attention and Feature Learning**  
        CBAM attention helps the classifier focus on important retinal regions, while graph-based learning can improve feature representation.

        **Final Output**  
        The system predicts the DR severity stage and provides visual evidence through lesion overlays.
        """
    )

with st.expander("How to connect a real model later"):
    st.code(
        """
# Example replacement idea
# 1. Load trained segmentation model
seg_model = load_model("models/unet_segmentation.h5")

# 2. Generate lesion mask
mask = seg_model.predict(preprocessed_image)

# 3. Load trained classifier
classifier = load_model("models/vit_cbam_classifier.h5")

# 4. Predict DR stage
prediction = classifier.predict(lesion_weighted_image)
        """,
        language="python",
    )

st.markdown("---")
st.caption("Built with Streamlit · Demo for AI healthcare portfolio/project presentation")
