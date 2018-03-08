# -*- coding:utf-8 -*-

count = 0
tmp = "abba"
lst2 = "aca"
lst1 = tmp
i = 0
while i <= (len(lst1)-1):
    lst1.insert(i, lst2)
    stop = False
    j = 0
    while j <= (len(lst1)-1)/2 and not stop:
        if j != lst1.pop():
            stop = True
        else:
            count += 1
    lst1 = tmp
