# -*- coding:utf-8 -*-
import os

Min = [x for x in range(12)]
VN = [1, 3, 5]
for i in range(1, 12, 1):
    for j in range(3):
        if VN[j] <= i and Min[i - VN[j]] + 1 < Min[i]:
            Min[i] = Min[i - VN[j]] + 1

print(Min[1:])

