import cv2
import numpy as np 
import matplotlib.pyplot as plt 

blk_size = 9        # 블럭 사이즈
C = 5               # 차감 상수 
img = cv2.imread('../img/alex.jpg', cv2.IMREAD_GRAYSCALE)

# Adaptive Gaussian Threshold만 적용
th_gauss = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                 cv2.THRESH_BINARY, blk_size, C)

# 결과 출력
plt.imshow(th_gauss, cmap='gray')
plt.title('Adaptive Gaussian Threshold')
plt.xticks([]), plt.yticks([])
plt.show()