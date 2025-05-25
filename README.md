# Number Plate Detection Using YOLOv8 🚗

This project implements a license plate recognition model using **YOLOv8**, trained on a custom dataset downloaded from Kaggle. The pipeline includes downloading, extracting, preprocessing, training, evaluating, and visualizing results for a YOLO-based object detection system in a Python environment.

---

## 📁 Dataset

- **Source**: [Number Plate Recognition Dataset on Kaggle](https://www.kaggle.com/datasets/abrahman97/number-plate-recognition-dataset)
- **Contents**:
  - `train/images`: Training images
  - `test/images`: Testing images
  - `valid/images`: Validation images
- **Labels**: YAML format with one class:
  ```yaml
  names:
    0: license_plate
  ```

---

## 🚀 Model & Training

- **Framework**: Ultralytics YOLOv8
- **Model Used**: yolov8n.pt (Nano version of YOLOv8 for speed and efficiency)

### Training Parameters
- **Epochs**: 40
- **Data Config**: datasets.yaml

### Sample Training Code
```python
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
result = model.train(data='datasets.yaml', epochs=40)
model.save('nbr-model.pt')
```

---

## 📊 Evaluation Metrics

After training, the model was evaluated using YOLO's built-in validation methods.

| Metric | Score |
|--------|-------|
| Precision | 0.9232 |
| Recall | 0.8894 |
| mAP@0.5 | 0.9318 |
| mAP@0.5:0.95 | 0.6220 |


## 📦 Environment

- **Python**: 3.x (Kaggle Docker Image)
- **Libraries**:
  - numpy
  - pandas
  - matplotlib
  - ultralytics
  - zipfile
  - os

---

## 🛠️ Setup Instructions

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/license-plate-detection-yolov8.git
   cd license-plate-detection-yolov8
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Authenticate with Kaggle API** (add credentials to environment variables):
   ```python
   import os
   os.environ['KAGGLE_USERNAME'] = 'your_kaggle_username'  # Replace with your username
   os.environ['KAGGLE_KEY'] = 'your_kaggle_api_key'        # Replace with your API key
   ```

4. **Download dataset**:
   ```bash
   kaggle datasets download abrahman97/number-plate-recognition-dataset
   ```

5. **Train the model**:
   ```python
   model.train(data='datasets.yaml', epochs=40)
   ```

---

## 📌 Notes

- This project was developed and tested on Kaggle Notebooks using its file system structure.
- Modify file paths if running locally or on a different platform.

---

## 📧 Contact

**Created by**: Talha Bin Shahid  
For questions or collaborations, reach out via [LinkedIn](https://linkedin.com/in/raja-talha) or [GitHub](https://github.com/talhabinshahid).

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Instructions for User:
1. Replace `yourusername` in GitHub URLs with your actual GitHub username.
2. Add paths to your accuracy visualization images (e.g., precision-recall curves, confusion matrices).
3. Update contact links (LinkedIn/GitHub) in the **Contact** section.
4. Ensure the `requirements.txt` file includes all necessary libraries.
