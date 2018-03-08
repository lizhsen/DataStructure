# -*- coding:utf-8 -*-

from pythonds.basic.stack import Stack
"""
Stack() 创建一个空的新栈。 它不需要参数，并返回一个空栈。
push(item)将一个新项添加到栈的顶部。它需要 item 做参数并不返回任何内容。
pop() 从栈中删除顶部项。它不需要参数并返回 item 。栈被修改。
peek() 从栈返回顶部项，但不会删除它。不需要参数。 不修改栈。
isEmpty() 测试栈是否为空。不需要参数，并返回布尔值。
size() 返回栈中的 item 数量。不需要参数，并返回一个整数。
"""

# s = Stack()
# print s.isEmpty()
# s.push(8)
# print s.isEmpty()
# print s.size()
# s.push(9)
# print s.size()
# print s.peek()
# print(s.items)


def firs_example():
    """
实现一个 mergeArray 函数，对两个已经排好序（从小到大）的数组进行排序（从小到大），数组里面是数字均为整数，
在 [0,100000) 之间，数组长度不超过 10000 。
输入数据有三行，第一行两个数字表示每个数组数字个数，后面两行分别表示两个数组
5,3
9,6,5,3,1
7,4,2
输出
1,2,3,4,5,6,7,9
    """

    tl1 = [9,6,5,3,1]
    tl2 = [7,4,2]
    for i in tl2:
        tl1.append(i)
    print tl1.sort()
    print tl1
    return tl1



firs_example()






