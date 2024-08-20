from skimage import io, img_as_float 
import numpy as np
from matplotlib import pyplot as plt 

my_image = io.imread("images/test_image.jpg")
#print(my_image)
print(my_image.min(), my_image.max())
#plt.imshow(my_image)

my_image[10:200, 10:200, :] = [255, 255, 0,255]  #Alpha da olduğu için biz sona 255 ekledik, 0 yazsaydık beyaz kare olurdu

plt.imshow(my_image)





"""
my_float_image = img_as_float(my_image)
print(my_float_image.min(), my_float_image.max())
plt.imshow(my_float_image) #my_image ile aynı
"""

"""
random_image = np.random.random([500, 500])
plt.imshow(random_image)
print(random_image.min(), random_image.max())
"""

