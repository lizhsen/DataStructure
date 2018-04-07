# -*- coding:utf-8 -*-
import cv2
import numpy as np
import datetime
from matplotlib import pyplot as plt

image = cv2.imread("C:/Users/lizhsen/Pictures/175855-001-C2.bmp")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.subplot(131), plt.imshow(image, "gray")
plt.title("source image"), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.hist(image.ravel(), 256)
plt.title("Histogram"), plt.xticks([]), plt.yticks([])
begin_t = datetime.datetime.now()
print begin_t
ret1, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)  #方法选择为THRESH_OTSU
# end_t = datetime.datetime.now()
plt.subplot(133), plt.imshow(th1, "gray")
plt.title("OTSU,threshold is " + str(ret1)), plt.xticks([]), plt.yticks([])
end_t = datetime.datetime.now()
plt.show()
print(end_t-begin_t)
