# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 11:16:36 2024

@author: GÖKHAN
"""

import cv2 
from skimage.filters import sobel

img = cv2.imread("images/test_image.jpg", 0) #open pictures as type 0: grayscale, 1: color 
img2 = sobel(img)  #sobel filter

cv2.imshow("pic", img) 
cv2.imshow("edge",img2)
print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()