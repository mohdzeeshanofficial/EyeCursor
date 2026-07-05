# 👁️ EyeCursor – Eye-Controlled Cursor Movement System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-red?logo=opencv&logoColor=white">
  <img src="https://img.shields.io/badge/MediaPipe-Face%20Mesh-orange">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask">
  <img src="https://img.shields.io/badge/PyAutoGUI-Automation-green">
  <img src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black">
</p>

<p align="center">
  <b>Control your computer using only your eyes.</b><br>
  Real-time eye tracking and blink detection powered by Computer Vision.
</p>

---

## 📖 Overview

**EyeCursor** is an AI-powered Human-Computer Interaction (HCI) project that allows users to control the mouse cursor using their eye movements and blink gestures. It leverages **OpenCV**, **MediaPipe Face Mesh**, **PyAutoGUI**, and **Flask** to provide a completely hands-free computer interaction experience.

The system detects facial landmarks in real time through a webcam, estimates the user's gaze direction, and translates eye movements into cursor movements. Eye blinks are recognized as mouse click events, enabling intuitive interaction without a physical mouse.

---

## ✨ Features

- 👁️ Real-time eye tracking
- 🖱️ Cursor movement using eyeball position
- 👆 Blink detection for mouse clicking
- 🎥 Live webcam processing
- ⚡ Fast and lightweight performance
- 🌐 Flask-based web interface
- 💻 Cross-platform support
- ♿ Accessibility-focused design

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Programming Language |
| 📷 OpenCV | Computer Vision |
| 👁️ MediaPipe Face Mesh | Facial Landmark Detection |
| 🖱️ PyAutoGUI | Mouse Automation |
| 🌐 Flask | Web Framework |
| 🎨 HTML5 | Frontend Structure |
| 🎨 CSS3 | Styling |
| ⚡ JavaScript | Client-side Interaction |

---


## Working Principle

The system continuously captures video from the user's webcam and processes it using MediaPipe Face Mesh to identify facial landmarks. Eye landmarks are analyzed to estimate gaze direction and map eye movements to screen coordinates. PyAutoGUI then controls the system cursor in real time. Blink detection is used to trigger mouse-click events, enabling complete cursor control without traditional input devices.

This project demonstrates the integration of computer vision, machine learning-based facial landmark detection, and automation tools to create an intuitive and accessible eye-controlled cursor system

## ⚙️ How It Works

1. Webcam captures live video.
2. OpenCV processes each video frame.
3. MediaPipe Face Mesh detects facial landmarks.
4. Eye landmarks are extracted.
5. Gaze direction is calculated.
6. Cursor coordinates are mapped.
7. PyAutoGUI moves the mouse cursor.
8. Blink detection performs mouse clicks.

---

## 📂 Project Structure

```
EyeCursor/
│
├── app.py
├── eye_control.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│
└── README.md
```

---

## 🚀 Applications

- Assistive Technology
- Accessibility Systems
- Human-Computer Interaction
- Smart Automation
- Touchless Computing
- Healthcare Assistance
- Research Projects

---

## 📌 Requirements

- Python 3.10+
- Webcam
- OpenCV
- MediaPipe
- Flask
- PyAutoGUI

Install dependencies:

```bash
pip install -r requirements.txt
pip instal opencv-contribe mediapipe flask and PyAutoGUI
```


---

## 🔮 Future Improvements

- Voice commands
- Multi-monitor support
- AI-based calibration
- Eye gesture shortcuts
- Drag-and-drop support
- Improved blink accuracy
- Custom sensitivity settings

---

## 👨‍💻 Developed By

**Mohd Zeeshan**

Computer Vision • OpenCV • Flask • MediaPipe • Python

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub!

---

## 📜 License

This project is licensed under the MIT License.
