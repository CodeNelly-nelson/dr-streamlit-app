from PIL import Image

from src.config import DR_STAGES
from src.services.segmentation_service import create_demo_segmentation_overlay
from src.services.classification_service import classify_demo_stage
from src.utils.image_utils import image_to_png_bytes


def run_demo_inference(image: Image.Image) -> dict:
    """
    Runs the full demo inference pipeline.

    Later, this function is where you can replace demo logic with:
    1. Real U-Net segmentation model
    2. Real ViT/CBAM/GCN classification model
    """

    overlay_image, lesion_scores = create_demo_segmentation_overlay(image)
    prediction, confidence, risk_level = classify_demo_stage(lesion_scores)

    return {
        "original_image": image,
        "overlay_image": overlay_image,
        "overlay_bytes": image_to_png_bytes(overlay_image),
        "lesion_scores": lesion_scores,
        "prediction": prediction,
        "confidence": confidence,
        "risk_level": risk_level,
    }
