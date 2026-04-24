# Diabetic Retinopathy Diagnosis System

A modular Streamlit web application that demonstrates an AI-powered diabetic retinopathy diagnosis workflow.

## What the App Demonstrates

This app follows a two-stage diagnostic pipeline:

1. **Lesion Segmentation**
   - Highlights lesion-like retinal regions
   - Demonstrates the role of U-Net-style segmentation

2. **Disease Stage Classification**
   - Predicts diabetic retinopathy severity
   - Demonstrates a ViT/attention-style classification workflow

> Note: This version uses simulated inference logic for demonstration. Real model files can be plugged into the service layer later.

## Project Structure

```text
dr_modular_streamlit_app/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   └── place trained model files here
│
├── data/
│   └── samples/
│
└── src/
    ├── config.py
    │
    ├── components/
    │   ├── header.py
    │   ├── sidebar.py
    │   ├── upload_panel.py
    │   └── results_panel.py
    │
    ├── services/
    │   ├── inference_service.py
    │   ├── segmentation_service.py
    │   └── classification_service.py
    │
    └── utils/
        └── image_utils.py
```

## Setup

```bash
python -m venv .venv
```

### Activate Environment

Mac/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run App

```bash
streamlit run app.py
```

## How to Connect Real Models Later

Replace the demo logic in:

```text
src/services/segmentation_service.py
src/services/classification_service.py
```

You can load trained models from the `models/` folder.

## Disclaimer

This application is for educational and demonstration purposes only. It is not a medical device and should not be used for clinical diagnosis.
