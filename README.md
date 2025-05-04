# YOLO Person Tracking Gimbal

A real-time person-tracking system using YOLO object detection, OpenCV, and an Arduino-powered servo gimbal. The camera follows the detected person by adjusting pan and tilt angles with two MG996R servo motors.

---

## 🔧 Features

- Real-time object detection using [Ultralytics YOLOv11](https://github.com/ultralytics/ultralytics)
- Tracks a single person using a webcam or Intel RealSense D435
- Sends tracking instructions over serial to an Arduino Uno
- 2-axis pan-tilt control using MG996R servos
- Modular code with clean separation between detection and hardware control

---

## 🧰 Hardware

| Component         | Description                     |
|------------------|---------------------------------|
| Arduino Uno       | Microcontroller for servo control |
| MG996R Servos (x2)| High-torque servo motors (Pan/Tilt) |
| Camera            | Intel RealSense D435 or USB webcam |
| Power Supply      | 5–6V @ 2A–3A (external servo power) |
| Pan/Tilt Bracket  | For mounting servos and camera  |
| Jumper wires      | For signal and power connections |

---

## 💻 Software

- Python 3.9
- [Ultralytics](https://pypi.org/project/ultralytics/)
- OpenCV
- pyserial
- Arduino IDE

---

## 🧠 How It Works

1. YOLO detects a person in each camera frame.
2. The center of the bounding box is compared to the center of the frame.
3. If the person is off-center, a direction command (`dx,dy`) is sent to the Arduino via serial.
4. The Arduino adjusts pan and tilt servo angles to re-center the person.

---

## 🔌 Wiring
<img width="740" alt="Screenshot 2025-05-04 at 4 38 27 PM" src="https://github.com/user-attachments/assets/79c035d8-8a08-4cea-af6c-f9197b9bddfc" />

- Pan Servo -> Arduino Pin 9
- Tilt Servo -> Arduino Pin 10
- Servo VCC -> External 5–6V Power Supply
- Servo GND -> Shared with Arduino GND

---

## 🚀 Getting Started

Follow these steps to clone the project, set up dependencies, and start tracking:

### 🧩 1. Clone the repository
1. ```git clone https://github.com/your-username/yolo-person-tracking-gimbal.git```
2. ```cd yolo-person-tracking-gimbal```
3. ```pip install -r requirements.txt```
4. Running Detection ```python detection.py```
5. Runing Tracking (Requires Arduino / Servos / External Camera) ```python tracking.py```

