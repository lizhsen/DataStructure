# -*- coding:utf-8 -*-
from skimage import data,filters
import matplotlib.pyplot as plt
image = data.camera("C:/Users/lizhsen/Pictures/175855-001-C2.bmp")
thresh = filters.threshold_otsu(image)   #返回一个阈值
dst =(image <= thresh)*1.0   #根据阈值进行分割

plt.figure('thresh',figsize=(8,8))

plt.subplot(121)
plt.title('original image')
plt.imshow(image,plt.cm.gray)

plt.subplot(122)
plt.title('binary image')
plt.imshow(dst,plt.cm.gray)

plt.show()
