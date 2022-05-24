from image_helper_functions import *
from preprocess_methods import *
import cv2
import pytesseract
from PIL import Image

path = "C:/Users/hp/Documents/major-project/Backend/images/" # image path

def preprocessing_pipeline(image,path):
    # is image shadowed
    image=shadow(image)
    save_image(image,'_first.png',path,)
    # noise removal
    image=denoise(image)
    save_image(image,'_first2.png',path,)
    contours = contour_detection(image)
    save_image(image,'_first3.png',path,)
    # save_image(contours,'_detected_document',path,)
    # is image grayscale
    # image = grayscale(image,path)
    
    # binarization
    # image = morphology(image)

    # edge detection
    # edges = edge_detection(image)

    # document detection
    # contour detection


    # skewness correction
    # deskew = skew_correction(image)
    # image = rotate(image, skew_correction(image), cval=1)
    # save_image(deskew,'_deskewed',path,)
    # save_image(image,'_first4.png',path,)

    # blur correction
    image = blur_correction(image)
    # save_image(sharpen, '_deblurred',path,)
    # save_image(image,'_first5.png',path,)

    
    # save_image(shadowed_img, '_shadow',path,)
    contours = contour_detection(image)
    save_image(image,'_last.png',path,)
    
    save_image(image,'_final1.png',path,)
    # display_image(image,"final")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
def get_string(img_path):
    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(img_path))

    # Remove template file
    #os.remove(temp)

    return result
def main():
    global path

    # load_image
    image = load_image('C:/Users/hp/Documents/major-project/Backend/images/Capture.PNG') #TODO: change img path
    # display_image(image,"Original")

    preprocessing_pipeline(image,path)
    print ('--- Start recognize text from image ---')
    print (get_string('C:/Users/hp/Documents/major-project/Backend/images/_final1.png'))

    print ("------ Done -------")



if __name__ == '__main__':
    main()