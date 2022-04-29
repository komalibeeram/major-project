import cv2
from image_helper_functions import *

def grayscale(image, path):
    if(len(image.shape)>=3):
        # convert to grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        save_image(image,"_grayscaled.png",path)
        return True
    return False