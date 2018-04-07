# -*- coding:utf-8 -*-
import datetime
import numpy as np
import cv2

def OTSU_enhance(img_gray, th_begin=0, th_end=256, th_step=1):
    assert img_gray.ndim == 2, "must input a gary_img"

    max_g = 0
    suitable_th = 0
    for threshold in xrange(th_begin, th_end, th_step):
        bin_img = img_gray > threshold
        bin_img_inv = img_gray <= threshold
        fore_pix = np.sum(bin_img)
        back_pix = np.sum(bin_img_inv)
        if 0 == fore_pix:
            break
        if 0 == back_pix:
            continue

        w0 = float(fore_pix) / img_gray.size
        u0 = float(np.sum(img_gray * bin_img)) / fore_pix
        w1 = float(back_pix) / img_gray.size
        u1 = float(np.sum(img_gray * bin_img_inv)) / back_pix
        # print u0, u1
        # intra-class variance
        g = w0 * w1 * (u0 - u1) * (u0 - u1)
        if g > max_g:
            max_g = g
            suitable_th = threshold
    return suitable_th


image = cv2.imread("C:/Users/lizhsen/Pictures/155906-002-C2.bmp")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
begin_t1 = datetime.datetime.now()
print OTSU_enhance(gray)
end_t1 = datetime.datetime.now()
print (end_t1 - begin_t1)
print '###########'
begin_t2 = datetime.datetime.now()
print OTSU_enhance(gray,0, 120,1)
end_t2 = datetime.datetime.now()
print (end_t2 - begin_t2)