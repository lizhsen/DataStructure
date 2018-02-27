# -*- coding: UTF-8 -*-

import time
import random

testlist = []
t1 = time.clock()
for j in range(10):
    k = random.randint(1, 1000)
    testlist.append(k)
t2 = time.clock()
# 找出其中第二大的数字

lar, sec = 0, 0
for i in testlist:
    if i == 0:
        pass
    if i > lar:
        sec = lar
        lar = i
    elif i > sec:
        sec = i
print lar, sec
print testlist
t3 = time.clock()
print (t3-t2), (t2-t1)