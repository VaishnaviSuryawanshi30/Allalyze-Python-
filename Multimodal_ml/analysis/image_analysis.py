import cv2
import os
import numpy as np

def analyze_image(path):
    img = cv2.imread(path)

    if img is None:
        return {"error": "Unable to read image"}

    height, width, channels = img.shape

    # Check color type
    image_type = "Grayscale" if channels == 1 else "Color"

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Mean brightness
    mean_brightness = float(np.mean(gray))

    # Edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Save edge image for display
    edge_path = path.replace(".", "_edges.")
    cv2.imwrite(edge_path, edges)

    # File size
    file_size_kb = round(os.path.getsize(path) / 1024, 2)

    return {
        "height": height,
        "width": width,
        "channels": channels,
        "image_type": image_type,
        "mean_brightness": round(mean_brightness, 2),
        "file_size_kb": file_size_kb,
        "edge_image_path": edge_path
    }
