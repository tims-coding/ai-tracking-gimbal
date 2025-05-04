import cv2
import serial
import time
from ultralytics import YOLO

# Serial port may vary; check with `ls /dev/tty.*` (Mac) or Device Manager (Windows)
arduino = serial.Serial('/dev/cu.usbmodem21401', 9600, timeout=1)
time.sleep(2)  # wait for Arduino to reset

model = YOLO("yolo11n.pt", task="detect")
cap = cv2.VideoCapture(0)

frame_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
center_x, center_y = frame_w // 2, frame_h // 2
dead_zone = 40  # pixels

def get_movement_direction(x, y):
    dx = 0
    dy = 0
    if abs(x - center_x) > dead_zone:
        dx = -1 if x > center_x else 1  # Inverted pan
    if abs(y - center_y) > dead_zone:
        dy = 1 if y > center_y else -1  # Tilt is probably fine
    return dx, dy

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(frame, classes=[0], verbose=False)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

            dx, dy = get_movement_direction(cx, cy)
            serial_cmd = f"{dx},{dy}\n"
            arduino.write(serial_cmd.encode())

            print(f"Person offset: dx={dx}, dy={dy}")
            break  # Only track one person

    cv2.imshow("Gimbal Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
arduino.close()
cv2.destroyAllWindows()
