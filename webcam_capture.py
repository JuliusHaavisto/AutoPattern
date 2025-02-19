import cv2
import os

def capture_image():
    """Captures an image from the webcam and saves it to /data"""
    
    print("Opening webcam...")
    cap = cv2.VideoCapture(0)  # Open webcam from default input

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Capturing image...")
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not capture image.")
        cap.release()
        return

    # For now images will be named by index, later maybe by timestamp(?
    image_index = 1
    while os.path.exists(f"data/captured_{image_index}.jpg"):
        image_index += 1
    image_path = f"data/captured_{image_index}.jpg"
    cv2.imwrite(image_path, frame)
    print(f"Image saved to {image_path}")

    cv2.imshow("Captured Image", frame)
    cv2.waitKey(8000)
    cv2.destroyAllWindows()

    cap.release()
    print("🔄 Webcam released.")

if __name__ == "__main__":
    print("Running webcam capture script...")
    capture_image()
    print("Image succesfully captured and stored")