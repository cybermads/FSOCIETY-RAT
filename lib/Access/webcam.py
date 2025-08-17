import cv2
from PIL import Image

def webcams():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        return None

    Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).save("webcam.png")
    return "webcam.png"

