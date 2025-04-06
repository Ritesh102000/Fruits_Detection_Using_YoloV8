# Fruits_Detection_Using_YoloV8
# 🍎 Real-Time Fruit Detection using YOLOv8

This project demonstrates a custom object detection model built using the YOLOv8 architecture to detect various types of fruits in real-time video streams. The entire pipeline includes data collection, manual annotation, training a YOLO model, evaluating its performance, and deploying it to work with a live webcam feed.

---

## 📸 Project Overview

- **Objective:** Detect and classify different fruits in real-time using a custom-trained YOLOv8 model.
- **Model Used:** YOLOv8s (small variant)
- **Platform:** Google Colab (for training and testing)
- **Deployment:** Real-time detection using webcam stream

---

## 🔧 Steps Involved

### 1. Data Collection & Annotation
- Captured multiple images of different fruit classes (e.g., apples, bananas, oranges, etc.)
- Annotated the images using tools like [LabelImg](https://github.com/tzutalin/labelImg)
- Saved annotations in YOLO format

### 2. Dataset Preparation
- Zipped the dataset and uploaded to Google Drive
- Mounted Google Drive in Colab and unzipped the dataset
- Used a Python script to split the data into training and validation sets (90/10 split)
- Generated a `data.yaml` configuration file based on the class labels

### 3. Model Training
- Installed the `ultralytics` package
- Trained a YOLOv8s model for **80 epochs** on **640x640** image resolution  
- Training command:
  ```bash
  yolo detect train data=data.yaml model=yolov8s.pt epochs=80 imgsz=640
### Model Evaluation

Ran predictions on the validation set using:

```bash
yolo detect predict model=runs/detect/train/weights/best.pt source=data/validation/images save=True
Visualized predictions with bounding boxes and labels.

Achieved a accuracy of 91.3% mAP on the validation dataset.

