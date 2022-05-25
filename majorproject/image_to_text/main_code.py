from .image_helper_functions import *
from .preprocess_methods import *
import cv2
import pytesseract
from PIL import Image
from gtts import gTTS
# from IPython.display import Audio
import nltk

path = "C:/Users/Soumya/Desktop/major-project/majorproject/image_to_text/images/" # image path

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

def clean_text(text):
    words = set(nltk.corpus.words.words())
    words = list(words) + ['chaitanya','bharathi','soumya','vemuri','murali','krishna']
    return " ".join(w for w in nltk.wordpunct_tokenize(text) if w.lower() in words or not w.isalpha())

def text_to_speech(text):
    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine
    myobj = gTTS(text,lang=language)

    # Saving the converted audio in a wav file named
    # welcome
    myobj.save("welcome.mp3")

def save_text(text):
    text = "".join(text)
    text_file = open('data.txt','w',encoding="utf-8")
    text_file.write(text)
    text_file.close()

def main(image_path):
    global path
    image_path='C:/Users/Soumya/Desktop/major-project/majorproject'+image_path
    print(image_path)
    # load_image
    image = load_image(image_path) #TODO: change img path
    # display_image(image,"Original")

    preprocessing_pipeline(image,path)
    print ('--- Start recognize text from image ---')
    text = get_string(path+'_final1.png')
    save_text(text)
    print ("------ Done -------")
    text = clean_text(text)
    text_to_speech(text)
    # Playing the converted file
    # Audio("welcome.mp3",autoplay=True)


