import random


def classify_demo_stage(lesion_scores: dict):
    """
    Demo classification logic.

    Replace this with real ViT/CBAM/GCN model inference later.
    """

    average_score = sum(lesion_scores.values()) / len(lesion_scores)

    if average_score < 25:
        prediction = "No DR"
        risk_level = "Low"
    elif average_score < 45:
        prediction = "Mild DR"
        risk_level = "Low-Medium"
    elif average_score < 65:
        prediction = "Moderate DR"
        risk_level = "Medium"
    elif average_score < 80:
        prediction = "Severe DR"
        risk_level = "High"
    else:
        prediction = "Proliferative DR"
        risk_level = "Very High"

    confidence = random.uniform(90.0, 98.9)

    return prediction, confidence, risk_level
