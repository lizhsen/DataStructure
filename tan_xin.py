# -*- coding:utf-8 -*-


def pay_min_num(n, value_num, m, value):
    # 取最小值：接下来最大面值硬币数量和钱数与该面值的比值，哪个小就把值赋给t，这个值就是当前面值的硬币应该取的数量，
    # 然后一一加起来得到最终的数量
    ans = 0
    for i in range(len(value)-1,-1,-1):
        t = min(n//value[i], value_num[i])
        n -= t * value[i]
        ans += t
    return ans


data_in = raw_input().strip().split(',')
n = int(data_in[0].split("=")[1])
value_num = []
for i in data_in[1:]:
    value_num.append(int(str(i).split("=")[1]))
value = [1, 5, 10, 20, 50, 100]
print (pay_min_num(n, value_num, 5, value))