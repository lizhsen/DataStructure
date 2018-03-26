# -*- coding:utf-8 -*-
def pay_ways_num(n, value_num, m, value):
    # 这是多少种方案的方法
    sum = 0
    arr =[]
    if n == 0:
        return sum
    if m < 0:
        return 0
    if n < 0:
        return 0
    for i in range(value_num[m]+1):
        pay_ways_num(n - i*value[m], value_num, m-1, value)
    return sum


data_in = raw_input().strip().split(',')
n = int(data_in[0].split("=")[1])
value_num = []
for i in data_in[1:]:
    value_num.append(int(str(i).split("=")[1]))
value = [1, 5, 10, 20, 50, 100]
print (pay_ways_num(n, value_num, 5, value))

