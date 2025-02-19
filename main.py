import cv2
import numpy as np
import os

from objectdetect import detected_objects, display_image
from objectcount import objectcount

def get_latest_image(folder_path="data"):
    """For finding the latest saved image from /data"""
    try:
        # Get all images
        image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".png"))]
        if not image_files:
            print("No images in the folder")
            return None
        
        latest_image = max(image_files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
        latest_image_path = os.path.join(folder_path, latest_image)
        print(f"Using the latest image: {latest_image_path}")
        return latest_image_path

    except Exception as e:
        print(f"Error: Cant find latest image: {e}")
        return None

def main():
    image_path = get_latest_image()
    if image_path:
        detected_image = detected_objects(image_path)
        count = objectcount(image_path)
        print(f"Total objects detected: {count}")

        if detected_image is not None:
            display_image(detected_image)
    else:
        print("No image found to count objects from")


if __name__ == "__main__":
    main()

