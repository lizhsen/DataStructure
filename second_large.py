# -*- coding: UTF-8 -*-

import time
import random

# testlist = []
# t1 = time.clock()
# for j in range(10):
#     k = random.randint(1, 1000)
#     testlist.append(k)
# t2 = time.clock()
# # 找出其中第二大的数字
#
# lar, sec = 0, 0
# for i in testlist:
#     if i == 0:
#         pass
#     if i > lar:
#         sec = lar
#         lar = i
#     elif i > sec:
#         sec = i
# print lar, sec
# print testlist
# t3 = time.clock()
# print (t3-t2), (t2-t1)


def reOrderArray(array):
    # write code here
    stack1=[]
    stack2=[]
    array = array
    for i in range(len(array) - 1):
        if array[i] % 2 == 1:
            stack1.append(array[i])
        else:
            stack2.append(array[i])
    for j in range(len(stack1) - 1):
        array[j] = stack1[j]
    for k in range(len(stack2) - 1):
        array[len(stack1) + k] = stack2[k]
    return array


print reOrderArray([1,3,5,7,2,4,6])