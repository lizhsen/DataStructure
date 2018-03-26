# -*- coding:utf-8 -*-
"""
第五套人民币纸币有1元，5元，10元，20元，50元，100元六个币种，小王去超市买东西，一共需要付款n元，a1张1元，a2张5元。。。a6张100元
小王共有多少种付款方式，没有则输出0
"""


def pay_ways_num(n, value_num, m, value):
    # 这是多少种方案的方法
    if n == 0:
        return 1
    if m < 0:
        return 0
    if n < 0:
        return 0
    time = 0
    for i in range(value_num[m]+1):
        # i 代表
        time = time + pay_ways_num(n - i*value[m], value_num, m-1, value)
    return time


data_in = raw_input().strip().split(',')
n = int(data_in[0].split("=")[1])
value_num = []
for i in data_in[1:]:
    value_num.append(int(str(i).split("=")[1]))
value = [1, 5, 10, 20, 50, 100]
print (pay_ways_num(n, value_num, 5, value))













