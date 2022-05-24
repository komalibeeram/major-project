import cv2
import numpy as np
from image_helper_functions import *

def contour_detection(edges):
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def locate_document(image, contours):
    try:
        areas=[]
        for c in contours:
            x,y,w,h = cv2.boundingRect(c)
            area = w*h
            if w>50 and h>50:
                dict = [area,{'area':area,'x':x,'y':y,'w':w,'h':h}]
                areas.append(dict)

        areas.sort(reverse=True)
        areas = areas[0]
        x = areas[1]['x']
        y = areas[1]['y']
        w = areas[1]['w']
        h = areas[1]['h']
        final_image = image[y:y+h,x:x+w]
    except:
        return image

    return final_image