# -*- coding:utf-8 -*-


def insert_sort(arr):
    count = len(arr)
    for i in range(1, count):
        key = arr[i]
        # 把arr里的值往形成的短序列里插
        j = i - 1
        while j >= 0:
            if key < arr[j]:
                arr[j+1], arr[j] = arr[j], key
            j -= 1
    print arr
    return arr


def bubble_sort(arr):
    count = len(arr)
    for i in range(count):
        for j in range(count - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    print arr
    return arr


def quick_sort(arr):
    """
    需要选择一个比较值key
    :param arr:
    :return:
    """
    count = len(arr)
    if count <= 1:
        return arr
    key = arr[count // 2]
    left = [x for x in arr if x < key]
    mid = [x for x in arr if x == key]
    right = [x for x in arr if x > key]
    return quick_sort(left) + mid + quick_sort(right)

# insert_sort([9,5,7,3,2,9,8])
# bubble_sort([9,5,7,3,2,9,8])
# print(quick_sort(([9,5,7,3,2,9,8])))
