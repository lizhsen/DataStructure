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

list1 = [1,3,4,6,3,2,1,1,9,10,2,2,6]
insert_sort(list1)

"""
链接：https://www.nowcoder.com/questionTerminal/e3dd485dd23a42899228305658457927
来源：牛客网

牛牛有一个鱼缸。鱼缸里面已经有n条鱼，每条鱼的大小为fishSize[i] (1 ≤ i ≤ n,均为正整数)，牛牛现在想把新捕捉的鱼放入鱼缸。鱼缸内存在着
大鱼吃小鱼的定律。经过观察，牛牛发现一条鱼A的大小为另外一条鱼B大小的2倍到10倍(包括2倍大小和10倍大小)，鱼A会吃掉鱼B。考虑到这个，牛牛要
放入的鱼就需要保证：
1、放进去的鱼是安全的，不会被其他鱼吃掉
2、这条鱼放进去也不能吃掉其他鱼
鱼缸里面已经存在的鱼已经相处了很久，不考虑他们互相捕食。现在知道新放入鱼的大小范围[minSize,maxSize](考虑鱼的大小都是整数表示),牛牛想
知道有多少种大小的鱼可以放入这个鱼缸。 
"""


# 暴力枚举
def howManyFishes(maxSize, minSize, n, fishSize):
    canput = False
    count = 0
    willFish = minSize
    while willFish < maxSize:
        for fish in fishSize:
            if minSize<=willFish and willFish


        willFish +=1










