import cv2
import numpy as np

def objectcount(image_path):
    """Counts the number of objects in an image using contour detection."""

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: No image found")
        return 0

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to make the image black and white
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    # Detect object boundaries
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Count the number of objects
    object_count = len(contours)

    # Draw bounding boxes around detected objects
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the detected objects
    cv2.imshow("Detected Objects", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return object_count  # Ensure return is inside the function
