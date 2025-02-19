import cv2
import os
import time
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load variables from env
load_dotenv()

# Retrieve Azure creds from env
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("CONTAINER_NAME", "captured-images")


# Initialize BlobServiceClient
try:
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    print("✅ Successfully connected to Azure Blob Storage!")
except Exception as e:
    print(f" Failed to connect to Azure Blob Storage: {e}")
    exit()

def capture_and_upload():
    """Captures an image from the webcam and uploads it to Azure Blob Storage."""
    
    print("Opening webcam...")
    cap = cv2.VideoCapture(0)  # Input from default (0)

    if not cap.isOpened():
        print("Error: Webcam not available.")
        return

    print("Capturing image...")
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not capture image.")
        cap.release()
        return

   
    # Generate a unique filename for captured image using timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")  # Format: YYYYMMDD-HHMMSS
    local_image_path = f"data/captured_{timestamp}.jpg"
    blob_name = f"captured_{timestamp}.jpg"

    # Save image also locally (For now this stays for debugging)
    cv2.imwrite(local_image_path, frame)
    print(f"Image saved locally as {local_image_path}")

    # Upload to Azure blob container storage
    try:
        print("Uploading image to Azure Blob Storage...")
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)

        with open(local_image_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"Image successfully uploaded to Azure as {blob_name}")

    except Exception as e:
        print(f"Upload failed: {e}")

    cap.release()
    print("Webcam closed")

if __name__ == "__main__":
    print("Running webcam capture and upload script...")
    capture_and_upload()
    print("Done.")
