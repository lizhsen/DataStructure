#coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n

    n = 5
    s = 9
    alist = [4,1,3,5,4]
    count = 0
    is_max = False
    blist = sorted(alist)
    value = s -alist[0]
    if value > alist[1]:
        value = value -alist[1]