from image_helper_functions import *
from grayscale import grayscale
from edge_detection import edge_detection
from contour_detection import contour_detection, locate_document
import cv2



path = "/images/username_image" # image path

def preprocessing_pipeline(image,path):

    # is image grayscale
    if grayscale(image,path):
        image = load_image(path+'_grayscaled.png')
    
    # edge detection
    edges = edge_detection(image)

    # document detection
    # contour detection
    contours = contour_detection(edges)
    image = locate_document(image, contours)
    save_image(image,'_detected_document',path,)

    # skewness correction

    # image scaling correction
    

    # blur correction

    # is image shadowed

    # binarization

    # noise removal

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    global path

    # load_image
    img = load_image(path+'_original.jpg')
    display_image(img,"Original")

    preprocessing_pipeline(image,path)

if __name__ == '__main__':
    main()