# -*- coding:utf-8 -*-


def insert_sort(arr):
    count = len(arr)
    for i in range(1, count):
        key = arr[i]
        # 就是从第一个元素作为初始列表，第二个元素与第一个元素比，形成一个2元素列表，之后第三个元素和2元素列表比，形成三元素列表。。。。
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


def selection_sort(arr):
    count = len(arr)
    # max_position = 0
    for i in range(count):
        max_position = 0
        for location in range(count - i - 1, 0, -1):
            if arr[location] > arr[max_position]:
                max_position = location
        tmp = arr[count - i - 1]
        arr[count - i - 1] = arr[max_position]
        arr[max_position] = tmp
    return arr


def shell_sort(arr):
    sub_arr_count = len(arr)//2
    while sub_arr_count > 0:
        for start_position in range(sub_arr_count):
            gap_insert_sort(arr, start_position, sub_arr_count)
        sub_arr_count = sub_arr_count//2
    return arr


def gap_insert_sort(arr, start, gap):
    for i in range(start+gap, len(arr), gap):
        current_value = arr[i]
        position = i
        while position >= gap and arr[position-gap] > current_value:
            arr[position] = arr[position-gap]
            position = position - gap
        arr[position] = current_value


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr


insert_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
# bubble_sort([9,5,7,3,2,9,8])
# print(quick_sort(([9,5,7,3,2,9,8])))
print(selection_sort(([54, 26, 93, 17, 77, 31, 44, 55, 20])))
print(shell_sort(([54, 26, 93, 17, 77, 31, 44, 55, 20])))
print(merge_sort(([54, 26, 93, 17, 77, 31, 44, 55, 20])))

