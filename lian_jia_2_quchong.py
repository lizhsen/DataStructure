# -*- coding:utf-8 -*-
import sys
"""
有一些数字，相互之间可能有重复，现在要对这些数进行去重，去重后还要排序。数字个数最多为1000个。
输出去重后的数字个数，并且输出排序后的数字
示例： 
输入 
10 
20 30 40 50 60 70 80 20 30 40
输出 
7 
20 30 40 50 60 70 80
"""
# n = input("请输入组数：")
# print ("请输入各组的人数：")
# group = sys.stdin.readline().strip().split(' ')
group = [20, 30, 40, 50, 60, 70, 80, 20, 30, 40]

def qsort(L):
    if len(L) < 2:
        return L
    pivot_element = L[len(L)//2]
    small = [i for i in L if i < pivot_element]
    large = [i for i in L if i > pivot_element]
    return qsort(small) + [pivot_element] + qsort(large)

print(len(qsort(group)))
print(qsort(group))


def sigle_sort(L):
    P = set(L)
    print(len(P))
    print sorted(P)


sigle_sort(group)