import numpy as np, cv2
import matplotlib.pylab as plt

img = cv2.imread('../img/like_lenna.png')

mask = np.zeros_like(img)
cv2.circle(mask, (260,210),100,(255,255,255), -1)

masked = cv2.bitwise_and(img, mask)

cv2.imshow('origial', img)
cv2.imshow('mask', mask)
cv2.imshow('masked',masked)
cv2.waitKey(0)
cv2.destroyAllWindows()