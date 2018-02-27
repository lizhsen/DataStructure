# -*- coding: UTF-8 -*-


# 99乘法表
def ninenine():
    for i in range(1, 10):
        k = 1
        while k <= i:
            print (str(k) + '*' + str(i) + '=' + str(k*i) + '\t')
            k += 1
    print '\n'


# 斐波那契
def feibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return feibo(n-1) + feibo(n-2)

# print feibo(2)


# 类似于斐波那契，跳阶梯
class Solution:
    def climbStairs(self, n):
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)

# ss = Solution()
# print ss.climbStairs(39)


def insert_sort(list1):
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            if list1[j] < list1[i]:
                k = list1[i]
                list1[i] = list1[j]
                list1[j] = k

    print(list1)
    return list1


list1 = [1, 3, 4, 6, 3, 2, 1, 1, 9, 10, 2, 2, 6]
insert_sort(list1)










