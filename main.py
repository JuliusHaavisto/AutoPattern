import cv2
import numpy as np

from objectdetect import detected_objects, display_image

def main():
    image_path = "data/triangle.jpg"
    detected_image = detected_objects(image_path)

    if detected_image is not None:
        display_image(detected_image)


if __name__ == "__main__":
    main()

