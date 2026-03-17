# Color-Detection-System
This project implements real-time color-based object detection using OpenCV. It converts input frames from BGR to HSV, computes dynamic color thresholds, and generates masks to isolate target colors. Morphological operations are applied to remove noise, and contour detection is used to identify and draw bounding boxes around detected objects.

# 1. Install dependencies
pip install opencv-python numpy

# 2. Run the project
python main.py

# 3. **Note on Colors**

- Currently detecting: Yellow

- You can change the color by modifying:

```
yellow = [0, 255, 255]  # BGR format
```
TO

```
[0, 0, 0]       # Black
[0, 165, 255]   # Orange
[255, 0, 0]     # Blue
[0, 255, 0]     # Green
```
