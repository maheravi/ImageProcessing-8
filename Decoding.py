import cv2
import numpy as np
psw = np.load('code.npy')

image = cv2.imread('encoded.jpg', cv2.IMREAD_GRAYSCALE)
row, cols = image.shape
result = np.zeros((row, cols), dtype='uint8')

for i in range(1, image.shape[0]-1):
    for j in range(1, image.shape[1]-1):
        result[i, j] = image[i, j] - psw[i, j]
        if result[i, j] < 0:
            result[i, j] = image[i, j]

cv2.imwrite('decoded.jpg', result)
cv2.imshow('decoded.jpg', result)
cv2.waitKey()
