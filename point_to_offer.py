# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         # write code here
#         print "递归"
#         if listNode is None:
#             return []
#         return self.printListFromTailToHead(listNode.next) + [listNode.val]
#
#
# s = Solution()
# p1 = ListNode(1)
# p2 = ListNode(2)
# p3 = ListNode(3)
# p1.next = p2
# p2.next = p3
# p3.next = None
#
# s.printListFromTailToHead(p1)


def max_m(a):
    """
    给定一个无序数组，包含正数、负数和0，要求从中找出3个数的乘积，使得乘积最大，要求时间复杂度：O(n)，空间复杂度：O(1)
输入描述:
    :param a:
    :return:
    """
    max1 = 0
    max2 = 0
    max3 = 0
    min1 =0
    min2 =0
    if len(a)<= 3:
        return a[0]*a[1]*a[2]
    for i in a:
        if i > max1:
            max3 = max2
            max2 = max1
            max1 = i
        elif i > max2:
            max3 = max2
            max2 = i
        elif i > max3:
            max3 = i
        elif i < min1:
            min2 = min1
            min1 = i
        elif i < min2:
            min2 = i
    if len(a) == 4:
        return max(min2*min1*max1,max1*max2*min2)
    if max3 == 0 or min2 == 0:
        return 0
    return max(min2*min1*max1,max1*max2*max3)
# n = int(raw_input())
# b = raw_input().strip().split(' ')
# a =[]
# for j in b:
#     a.append(int(j))
# print(max_m(a))

def merge_s(h,w,n,m):
    h = sorted(h)
    w = sorted(w)
    i = 0
    j = 0
    while i < n and j < m:
        if w[j] >= h[i]:
            j += 1
            i += 1
        else:
            j += 1
    return i
# n = int(raw_input())
# h = raw_input().strip().split(' ')
# m = int(raw_input())
# w = raw_input().strip().split(' ')
# child=[]
# choclete=[]
# for k in h:
#     child.append(int(k))
# for x in w:
#     choclete.append(int(x))
#
# print(merge_s(child,choclete,n,m))

# b = raw_input().strip().split(' ')
# arr = []
# res = [0]
# for i in b:
#     arr.append(int(i))
# if len(arr) <= 1:
#     print 0
# else:
#     for j in range(1,len(arr)):
#         count = 0
#         for k in range(j-1):
#             if arr[j]> arr[k]:
#                 count += 1
#         res.append(count)
#     print res

arr = [1,2, 3,2,2,2,2,2,5,7]
res = []
is_has = False
# # b = raw_input().strip().split(' ')
# for i in b:
#     arr.append(int(i))
no_repeat = set(arr)
for i in no_repeat:
    res.append(i)
num = [0] * len(res)
for j in arr:
    for k in range(len(res)):
        if j == res[k]:
            num[k] += 1
for m in range(len(res)):
    if num[m] > len(arr)/2:
        is_has = True
        print res[m]
    else:
        pass
if not is_has:
    print 0


b = raw_input().strip().split(' ')
arr = []
is_has = False
for i in b:
    arr.append(int(i))
no_repeat = set(arr)
for i in no_repeat:
    res.append(i)
num = [0] * len(res)
for j in arr:
    for k in range(len(res)):
        if j == res[k]:
            num[k] += 1
for m in range(len(res)):
    if num[m] > len(arr)/2:
        is_has = True
        print res[m]
    else:
        pass
if not is_has:
    print 0