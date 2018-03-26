import sys

def fun():
    line = sys.stdin.readline().strip().split()
    arr = []
    res = [0]
    for i in line:
        arr.append(int(i))
    if len(arr) <= 1:
        return 0
    else:
        for j in range(1, len(arr)):
            count = 0
            for k in range(j):
                if arr[j] > arr[k]:
                    count += 1
            res.append(count)
    return res
print(fun())

