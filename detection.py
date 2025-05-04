from ultralytics import YOLO

# Load the model
model = YOLO("yolo11n.pt", task="detect")

# Run inference using your webcam (device 0)
model.predict(source=0, show=True)
