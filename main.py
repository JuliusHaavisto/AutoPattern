import cv2
import numpy as np

from objectdetect import detected_objects, display_image
from objectcount import objectcount
def main():
    image_path = "data/triangle.jpg"
    detected_image = detected_objects(image_path)
    count = objectcount(image_path)
    print(f"Total objects detected: {count}")

    if detected_image is not None:
        display_image(detected_image)


if __name__ == "__main__":
    main()

