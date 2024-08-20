# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:09:16 2024

@author: GÖKHAN
"""

import numpy as np # matris işlemleri yapabilmek için numpy kütüphanesi
from skimage import io #görseli açıp okumak, kaydetmek için skimage kütüphanesi

img = io.imread('images/test_image.jpg') #görseli oku
print(img) #görseli numpy array olarak ekrana bas
print(img.dtype, img.shape) #array'in tipi ve boyutunu ekrana bas -> uint8 (511, 639, 4)

img_rgb = img[:, :, :3] #görseli okuduğumuzda 4 kanal olduğunu görüyoruz yalnızca ilk üçünü (RGB) seçiyoruz. alpha kanalını yok sayıyoruz
img_tinted = img_rgb * [0., 0., 1.] #matristeki her bir pikseli buradaki değerlerle çarpıyoruz
# R (Red: Kırmızı) = 0, G (G: Green) = 0, B (Blue: Mavi) = 1 * değeri oldu yani sadece mavileri göreceğiz.
img_tinted = img_tinted.astype(np.uint8) #resim dosyaları genellikle uint8 tipindedir. float64 geldiği için bunu dönüştürüyoruz.
io.imsave('images/tinted.jpg', img_tinted) #mavilerin kaldığı görüntüyü kaydediyoruz