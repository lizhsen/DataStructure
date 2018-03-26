# -*- coding:utf-8 -*-
def findnum(x):
    s = 0
    for i in range(1,a+1):
        if x//i >= b:
            s = s+b
        else:
            s = s+x//i
    return s


a,b,c = raw_input().split()
a,b,c = map(int,[a,b,c])
low = 1
hight = a*b
while (low<=hight):
    middle = (low+hight)//2
    par = findnum(middle)
    if par < c:
        low = middle + 1
    else:
        hight = middle - 1
print low


