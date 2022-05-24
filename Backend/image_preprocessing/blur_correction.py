import cv2
import numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('/content/blur2.jfif')
print('before')
cv2_imshow(image)
# [[0, -1, 0],[-1, 5,-1],[0, -1, 0]]
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(image, -1, sharpen_kernel)
print('sharpen1')
cv2_imshow( sharpen)
# sharpen_kernel2 = np.array([[0, -1, 0],[-1, 5,-1],[0, -1, 0]])
# sharpen2 = cv2.filter2D(image, -1, sharpen_kernel2)
# print('sharpen2')
# cv2_imshow( sharpen2)
cv2.waitKey()