from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model('resources/us.jpg',show=True)
