import cv2
import numpy as np
import random

image = cv2.imread('EP-IBB.jpg', cv2.IMREAD_GRAYSCALE)
row, cols = image.shape
psw = np.zeros((row, cols), dtype='uint8')
result = np.zeros((row, cols), dtype='uint8')

for i in range(1, psw.shape[0]-1):
    for j in range(1, psw.shape[1]-1):
        psw[i, j] = random.randint(0, 256)
        result[i, j] = image[i, j] + psw[i, j]
        if result[i, j] > 255:
            result[i, j] = image[i, j]

cv2.imwrite('encoded.jpg', result)
np.save('code.npy', psw)
