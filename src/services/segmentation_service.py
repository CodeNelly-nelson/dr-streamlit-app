from PIL import Image, ImageDraw
import random

from src.config import LESION_CLASSES


def create_demo_segmentation_overlay(image: Image.Image):
    """
    Creates a simulated lesion overlay.

    Replace this file later with real U-Net model inference.
    """

    overlay = image.copy().convert("RGBA")
    draw = ImageDraw.Draw(overlay, "RGBA")

    width, height = overlay.size

    lesion_colors = {
        "Microaneurysms": (0, 80, 255, 110),
        "Hemorrhages": (255, 0, 0, 110),
        "Hard Exudates": (255, 220, 0, 120),
        "Soft Exudates": (0, 180, 80, 110),
    }

    lesion_scores = {}

    for lesion_name in LESION_CLASSES:
        score = random.uniform(15, 95)
        lesion_scores[lesion_name] = score

        number_of_marks = random.randint(3, 8)

        for _ in range(number_of_marks):
            x = random.randint(int(width * 0.20), int(width * 0.80))
            y = random.randint(int(height * 0.20), int(height * 0.80))
            radius = random.randint(8, max(10, int(min(width, height) * 0.035)))

            color = lesion_colors[lesion_name]
            draw.ellipse(
                (x - radius, y - radius, x + radius, y + radius),
                fill=color,
                outline=color,
            )

    return overlay.convert("RGB"), lesion_scores
