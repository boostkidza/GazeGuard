# GazeGuard
Eye Recognition Based Attendance System

Absolutely! Here's a GitHub-style **README.md layout** for your **GazeGuard** project, written just like your friend's biomedical inventory repo—with sections like **Project Description**, **Features**, **Technology Used**, **How It Works**, and more.

---

### 📄 Final `README.md` for **GazeGuard** (GitHub Style)

```markdown
# GazeGuard 👁️🛡️
An Eye Recognition Based Attendance System using Python, Flask, and MongoDB.

---

## 📌 Project Description

GazeGuard is a contactless attendance system that leverages eye recognition to authenticate users and mark their attendance. It uses computer vision to capture and compare eye images, offering a secure, hygienic alternative to traditional biometric systems. The application supports integration with Android phone cameras for real-time image input via IP Webcam.

The system consists of:
- A web-based interface (built with Flask + HTML)
- A backend for capturing and comparing eye images
- MongoDB for storing user and attendance data

---

##✨ Features

- 👁️ Eye-based user registration and attendance marking
- 📷 Live camera feed using Android IP Webcam app
- 🔐 Secure image matching (only eye region is compared)
- 💾 MongoDB database integration
- 🌐 HTML interface for ease of use
- 📁 All captured images are stored locally (optional)
- 💡 Simple and modular codebase

---

## ⚙️ Technology Used

- **Python**
- **Flask**
- **OpenCV**
- **MongoDB**
- **PyMongo**
- **HTML5/CSS3**
- **IP Webcam (Android App)**

---

## 🧠 How It Works

1. **Registration:** Users register by scanning their eyes using a camera. Eye images are saved with user IDs in MongoDB.
2. **Attendance:** On login, the system captures a new eye image and compares it to existing ones.
3. **Matching:** If a match is found, attendance is recorded in the database.

---

## 🗂️ Folder Structure

```
GazeGuard/
├── app.py                   # Main Flask app
├── templates/
│   └── index.html           # UI for registration/attendance
├── static/
│   └── style.css            # Basic styling
├── eye_images/              # Eye image storage (optional)
├── utils/
│   └── eye_matcher.py       # Eye recognition logic
├── requirements.txt         # Required Python libraries
├── .gitignore               # Files/folders to ignore
└── README.md                # Project documentation
```

---

## 🚀 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/GazeGuard.git
cd GazeGuard
```

### 2. Create virtual environment (optional)
```bash
python -m venv venv
source venv/bin/activate       # For Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask server
```bash
python app.py
```

### 5. Access in browser
Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📷 IP Webcam Configuration (for Android Users)

1. Install [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam) app on your Android phone
2. Start the server in the app
3. Note the IP address (e.g., `http://192.168.x.x:8080/video`)
4. Replace the video URL in `app.py` with your IP stream

---

## 📋 Future Scope

- Real-time attendance dashboard
- Attendance logs export to CSV
- Enhanced UI/UX with Bootstrap
- Accuracy improvements in eye recognition

---

## 📜 License

This project is licensed under the [MIT License](LICENSE)

---

## 🙌 Acknowledgements

- Python community
- OpenCV contributors
- Flask documentation
- IP Webcam Android app

```

---

### ✅ To Use It:

1. Create a file `README.md` in your project folder
2. Copy and paste the above content into it
3. When you push the repo to GitHub, this will display beautifully on the main page
