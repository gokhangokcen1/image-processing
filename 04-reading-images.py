#pillow 
from PIL import Image
import numpy as np

img = Image.open("images/test_image.jpg")
print(type(img))

#img.show()
print(img.format) #png

img1 = np.asarray(img)
print(type(img1)) #nump.ndarray

######################################################

#Matplotlib
#pyplot
 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread("images/test_image.jpg")
#print(type(img))
#♦print(img.shape) #511 satır, 639 sütun, 4 resim
plt.imshow(img)
plt.colorbar()

######################################################

#scikit-image

from skimage import io, img_as_float, img_as_ubyte
import matplotlib.pyplot as plt

image = io.imread("images/test_image.jpg")
#print(type(image))
#plt.imshow(image)
#print(image) #matris
image_float = img_as_float(image)
print(image_float)

######################################################

#opencv-python

import cv2
from matplotlib import pyplot as plt
grey_img = cv2.imread("images/test_image.jpg",0)
color_img = cv2.imread("images/test_image.jpg",1) #orijinal resim

#plt.imshow(img) #opencv RGB değil BGR olduğu için renkler değişiyor
plt.imshow(cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB))

cv2.imshow("Grey Image",grey_img )
cv2.imshow("Color Image", color_img) 
cv2.waitKey(0)

cv2.destroyAllWindows()

######################################################

# reading all images - glob

import cv2 
import glob 

path = "images/test_images/aeroplane/*"

for file in glob.glob(path):
    print(file)
    a = cv2.imread(file)
    print(a)
    cv2.imshow("Original Image", a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    c = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    cv2.imshow("Color Image", c)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



