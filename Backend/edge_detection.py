import cv2
import numpy as np
from image_helper_functions import *

def edge_detection(image):
    kernel = np.ones((5,5),'uint8')
    image = cv2.dilate(image,kernel,iterations=1)
    edges = cv2.Canny(image, 100, 70)
    return edges