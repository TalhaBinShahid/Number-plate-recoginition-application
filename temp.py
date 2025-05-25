from ultralytics import YOLO
import cv2

# Load model
model = YOLO('nbr-model.pt')

# Inference
results = model.predict('input_img3.jpeg')

# Extract and print results
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        conf = box.conf[0].item()
        cls_id = int(box.cls[0])
        print(f"Detected plate at ({x1}, {y1}, {x2}, {y2}), confidence: {conf:.2f}")

# Visualize
annotated_frame = results[0].plot()
cv2.imshow('Result', annotated_frame)
cv2.waitKey(0)