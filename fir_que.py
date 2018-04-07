# coding=utf-8
import sys

a = sys.stdin.readline().split()
n = int(a[0])
k = int(a[1])
arr = sys.stdin.readline().split()
b = []

count = 0
if len(arr) <= 1:
    print count
else:
    for i in range(len(arr)-1):
        stop = False
        j = i + 1
        while j < len(arr) and not stop:
            if int(arr[j]) - int(arr[i]) == k or int(arr[i]) - int(arr[j]) == k:
                count += 1
                b.append(arr[i])
                b.append(arr[j])
                stop = True
            j += 1
