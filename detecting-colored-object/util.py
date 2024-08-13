import numpy as np
import cv2

def get_limits(color):
    # Renk verisini 1x1x3 boyutunda bir numpy dizisine dönüştür
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    
    # Renkin alt ve üst limitlerini belirle
    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255
    
    # Limitleri numpy dizilerine dönüştür
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)
    
    return lowerLimit, upperLimit
