
import cv2
import os
import time
import pymongo
import numpy as np
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["attendance_db"]
users_collection = db["users"]
attendance_collection = db["attendance"]

# Eye detection cascade
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# IP camera URL (change this to your phone's IP Webcam URL)
IP_CAMERA_URL = "http://192.168.0.108:8080/video"


def capture_eye_image():
    cap = cv2.VideoCapture(IP_CAMERA_URL)

    # Wait for camera to start
    start_time = time.time()
    while not cap.isOpened():
        if time.time() - start_time > 5:
            print("Error: Camera not responding.")
            return None

    # Skip initial frames to stabilize
    for _ in range(5):
        ret, frame = cap.read()

    # Capture image
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        return None

    # Detect eyes
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

    if len(eyes) > 0:
        x, y, w, h = eyes[0]
        eye_image = frame[y:y + h, x:x + w]
        cap.release()
        return eye_image
    else:
        print("No eyes detected. Try again.")
        cap.release()
        return None


def save_eye_image(user_name, eye_image):
    os.makedirs("eye_images", exist_ok=True)
    eye_image_path = f"eye_images/{user_name}.jpg"
    cv2.imwrite(eye_image_path, eye_image)
    return eye_image_path


def register_user(user_name):
    eye_image = capture_eye_image()
    if eye_image is not None:
        eye_image_path = save_eye_image(user_name, eye_image)
        users_collection.insert_one({"name": user_name, "eye_image": eye_image_path})
        print(f"User {user_name} registered successfully.")
    else:
        print("User registration failed. Try again.")


def compare_eyes(eye_image, stored_image_path):
    stored_image = cv2.imread(stored_image_path, cv2.IMREAD_GRAYSCALE)
    eye_gray = cv2.cvtColor(eye_image, cv2.COLOR_BGR2GRAY)
    stored_resized = cv2.resize(stored_image, (eye_gray.shape[1], eye_gray.shape[0]))
    difference = np.sum((eye_gray - stored_resized) ** 2)
    return difference < 1000000  # Threshold for similarity


def mark_attendance(user_name):
    user = users_collection.find_one({"name": user_name})
    if user:
        eye_image = capture_eye_image()
        if eye_image is not None:
            stored_image_path = user["eye_image"]
            if compare_eyes(eye_image, stored_image_path):
                attendance_collection.insert_one({"name": user_name, "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')})
                print(f"Attendance marked for {user_name}.")
            else:
                print("Eye scan does not match. Try again.")
        else:
            print("Failed to capture eye image.")
    else:
        print("User not found. Please register first.")


if __name__ == "__main__":
    while True:
        print("\n1. Register User\n2. Mark Attendance\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            user_name = input("Enter your name: ")
            print(f"Look at the camera to register, {user_name}...")
            register_user(user_name)
        elif choice == "2":
            user_name = input("Enter your name: ")
            print(f"Look at the camera for attendance, {user_name}...")
            mark_attendance(user_name)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

