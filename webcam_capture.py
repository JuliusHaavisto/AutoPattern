import cv2

def capture_image():
    """Capturing image using the webcam (0) and saving it in to the /data folder"""

    # Open webcam from default (0) input
    cap = cv2.VideoCapture(0)
    
    # Error handling
    if not cap.isOpened():
        print("Error: Webcam not connected")
        return
    
    # Capture a single frame from webcam (0) feed
    ret, frame = cap.read()
    if not ret:
        print("Error: Cant capture image")
        cap.release()
        return
    
    # Saving captured image to /data
    image_path = "data/captured__image.jpg"
    cv2.imwrite(image_path, frame)
    print(f"Image saved to {image_path}")

    # Show the captured image
    cv2.imshow("Captured image", frame)
    cv2.waitKey(8000)
    cv2.destroyAllWindows()

    # Stop webcam
    cap.release()

if __name__ == "__main__":
    capture_image    