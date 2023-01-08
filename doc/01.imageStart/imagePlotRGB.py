#-*- coding:utf-8 -*-
import cv2
from matplotlib import pyplot as plt # as는 alias 적용시 사용

img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.axis('off') # 창의 x축 y축 제거
plt.imshow(img2)
plt.show()
