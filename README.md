# EyeCursor – Eye-Controlled Cursor Movement System

EyeCursor is a computer vision-based Human-Computer Interaction (HCI) project that enables users to control the mouse cursor using eye movements and blink gestures. The system utilizes real-time facial landmark detection to track eye positions through a webcam and translate them into cursor movements on the screen.

Built using OpenCV, MediaPipe, PyAutoGUI, and Flask, the application captures live video frames, detects facial and eye landmarks, calculates gaze direction, and moves the cursor accordingly. Eye blinks can be used to perform mouse click actions, providing a hands-free computing experience.

## Features

 👁️ Real-time eye tracking
 🖱️ Cursor movement using eyeball position
 👆 Blink detection for mouse clicking
 🎥 Live webcam processing
 ⚡ Fast and lightweight performance
 🌐 Flask-based web interface
 💻 Cross-platform support
 ♿ Accessibility-focused design

## Technologies Used

* Python
* OpenCV
* MediaPipe Face Mesh
* PyAutoGUI
* Flask
* HTML, CSS, JavaScript

## Applications

* Assistive technology for individuals with physical disabilities
* Hands-free computer interaction
* Accessibility-focused user interfaces
* Human-Computer Interaction (HCI) research
* Smart control systems and automation

## Working Principle

The system continuously captures video from the user's webcam and processes it using MediaPipe Face Mesh to identify facial landmarks. Eye landmarks are analyzed to estimate gaze direction and map eye movements to screen coordinates. PyAutoGUI then controls the system cursor in real time. Blink detection is used to trigger mouse-click events, enabling complete cursor control without traditional input devices.

This project demonstrates the integration of computer vision, machine learning-based facial landmark detection, and automation tools to create an intuitive and accessible eye-controlled cursor system.




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
```

Run the project:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 📸 Demo

Add screenshots or GIFs here.

```
/screenshots/homepage.png
/screenshots/demo.gif
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
