# -*- coding:utf-8 -*-

from pythonds.basic.queue import Queue

"""
Queue() 创建一个空的新队列。 它不需要参数，并返回一个空队列。
enqueue(item) 将新项添加到队尾。 它需要 item 作为参数，并不返回任何内容。
dequeue() 从队首移除项。它不需要参数并返回 item。 队列被修改。
isEmpty() 查看队列是否为空。它不需要参数，并返回布尔值。
size() 返回队列中的项数。它不需要参数，并返回一个整数。
"""


def first_example(num):
    """
    题目描述
假设有一个有 n 个元素的数组，求该数组右移 k 个元素后的数组，要求算法的空间复杂度为 O(1) 。
输入数据右三行，第一行表示数组元素个数 n ，第二行表示数组，第三行表示 k
7
1,2,3,4,5,6,7
3
输出
5,6,7,1,2,3,4
    """
    q = Queue()
    tl1 = [1,2,3,4,5,6,7]
    tl1.reverse()

    for i in tl1:
        q.enqueue(i)
    print q.items
    while num > 0:
        q.enqueue(q.dequeue())
        num -= 1
    print(q.items)
    return q


def second_example(num):
    """
        题目描述
    假设有一个有 n 个元素的数组，求该数组右移 k 个元素后的数组，要求算法的空间复杂度为 O(1) 。
    输入数据右三行，第一行表示数组元素个数 n ，第二行表示数组，第三行表示 k
    7
    1,2,3,4,5,6,7
    3
    输出
    5,6,7,1,2,3,4
        """
    tl2 = [1, 2, 3, 4, 5, 6, 7]
    while num > 0:
        tl2.insert(0, tl2.pop())
        num -= 1
    print(tl2)
    return tl2


first_example(3)
second_example(3)

