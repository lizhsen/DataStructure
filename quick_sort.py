# -*- coding:utf-8 -*-
def gap_insert_sort(arr, start, gap):
    for i in range(start+gap, len(arr),gap):
        current_value = arr[i]
        position = i
        while position >= gap and arr[position -gap] > current_value:
            arr[position] = arr[position -gap]
            position = position -gap
        arr[position] = current_value


def shell_sort(arr):
    step = len(arr)//2
    while step > 0:
        for i in range(step):
            gap_insert_sort(arr,i, step)
        step = step//2
    return arr


# print(shell_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))


def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr


# print(bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
def selection_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        max_position = i
        for j in range(i):
            while arr[j] > arr[max_position]:
                max_position = j
        tmp = arr[i]
        arr[i] = arr[max_position]
        arr[max_position] = tmp
    return arr


# print(selection_sort([1, 26, 93, 17, 17, 31, 44, 55, 1]))
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > key:
                arr[j+1] = arr[j]
                arr[j] = key
            j -= 1
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr











print(merge_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))

