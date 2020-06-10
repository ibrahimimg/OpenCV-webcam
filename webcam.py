#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 07:07:27 2020

@author: ibrahim
"""

import sys
import cv2

input_source=0
video_capture = cv2.VideoCapture(input_source)

while video_capture.isOpened():
    key_pressed = cv2.waitKey(60)
    # Capture frame-by-frame
    flag, frame = video_capture.read()
    # Display the resulting frame
    cv2.imshow('Video', frame)
    # exit if esc key is pressed
    if key_pressed == 27:
        break

#release the capture
video_capture.release()
