# -*- coding:utf-8 -*-

# list1 = input("请输入你需要的列表:" )
# length1 = input("请输入长度：")
"""
Deque() 创建一个空的新 deque。它不需要参数，并返回空的 deque。
addFront(item) 将一个新项添加到 deque 的首部。它需要 item 参数 并不返回任何内容。
addRear(item) 将一个新项添加到 deque 的尾部。它需要 item 参数并不返回任何内容。
removeFront() 从 deque 中删除首项。它不需要参数并返回 item。deque 被修改。
removeRear() 从 deque 中删除尾项。它不需要参数并返回 item。deque 被修改。
isEmpty() 测试 deque 是否为空。它不需要参数，并返回布尔值。
size() 返回 deque 中的项数。它不需要参数，并返回一个整数。
"""
from pythonds.basic.deque import Deque


def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

count = 0
str1 = 'abba'
str2 = 'cdc'

str_lst = list(str1)
for i in range(len(str_lst)):
    j = len(list(str2))-1
    while j >= 0:
        str_lst.insert(i, list(str2)[j])
        j -= 1
    print str_lst
    if palchecker(str_lst):
        count += 1
    str_lst = list(str1)
    i += 1
print count



