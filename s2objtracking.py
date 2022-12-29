import cv2
import time
import math
video = cv2.VideoCapture("bb3.mp4")
# Read the first frame of the video
returned, img = video.read()
# Load tracker 
tracker = cv2.TrackerCSRT_create()
# Select the bounding box on the image
bbox = cv2.selectROI("Tracking", img, False)
# Initialise the tracker on the img and the bounding box
tracker.init(img, bbox)

print(bbox)