import cv2
import numpy as np

def detected_objects(image_path):
    """Only simulating object detection using edge detection """
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found")
        return None
    

    # 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny (gray, 30, 100)

    return edges

def display_image(image):
    """Displays the image"""
    cv2.imshow("Detected Objects", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

