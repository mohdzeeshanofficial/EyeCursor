# EyeCursor – Eye-Controlled Cursor Movement System

EyeCursor is a computer vision-based Human-Computer Interaction (HCI) project that enables users to control the mouse cursor using eye movements and blink gestures. The system utilizes real-time facial landmark detection to track eye positions through a webcam and translate them into cursor movements on the screen.

Built using OpenCV, MediaPipe, PyAutoGUI, and Flask, the application captures live video frames, detects facial and eye landmarks, calculates gaze direction, and moves the cursor accordingly. Eye blinks can be used to perform mouse click actions, providing a hands-free computing experience.

## Features

* Real-time eye tracking using webcam input
* Cursor movement based on eyeball position
* Blink detection for mouse clicking
* Lightweight and responsive interface
* Flask-powered web application for easy interaction
* Cross-platform support (Windows, Linux, macOS)

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
