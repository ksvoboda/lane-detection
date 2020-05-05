import argparse
import os.path as ops
import time

import cv2
import glog as log
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("data/tusimple_test_image/0.jpg")

cv2.imshow('image', image)
cv2.waitKey(0)