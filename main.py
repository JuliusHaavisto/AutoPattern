import cv2
import numpy as np

def test_camera():
    print("Testing OpenCV...")

    # Create a black image (simulating a camera frame)
    frame = np.zeros((500, 500, 3), dtype=np.uint8)

    # Draw a white circle in the middle
    cv2.circle(frame, (250, 250), 50, (255, 255, 255), -1)

    # Show the test image
    cv2.imshow("OpenCV Test Frame", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_camera()