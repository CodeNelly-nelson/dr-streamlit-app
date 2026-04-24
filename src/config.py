APP_TITLE = "Diabetic Retinopathy Diagnosis System"

APP_DESCRIPTION = """
A modular Streamlit demo showing a two-stage AI pipeline:
lesion segmentation followed by diabetic retinopathy stage classification.
"""

DR_STAGES = [
    "No DR",
    "Mild DR",
    "Moderate DR",
    "Severe DR",
    "Proliferative DR",
]

LESION_CLASSES = {
    "Microaneurysms": "Small red dots caused by tiny blood vessel bulges.",
    "Hemorrhages": "Blood leakage spots in the retina.",
    "Hard Exudates": "Yellowish lipid deposits linked to vascular leakage.",
    "Soft Exudates": "Cotton-wool spots caused by nerve fiber layer damage.",
}

DEMO_CONFIDENCE_RANGE = (90.0, 98.9)
