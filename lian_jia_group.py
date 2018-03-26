# -*- coding:utf-8 -*-
import sys
"""
题目描述
小组编号问题。输入一组数【2,7,3,4,9】，表示第一组有2个人，编号为【1、2】，第二组有7个人编号为【3~9】，第三组有3个人编号为【10~12】，第四组有4个人编号为【13~16】，第五组有9个人编号为【17~25】。
现在求，编号为1、25、11的人分别在哪个组里。
示例： 
输入 
5 
2 7 3 4 9 
3 
1 25 11
输出 
1 5 3
"""
# n = input("请输入组数：")
# print ("请输入各组的人数：")
# group = sys.stdin.readline().strip().split(' ')
# print ("请输入要查找的人数：")
# m = sys.stdin.readline().strip()
# print ("请输入要查找的人的编号：")
# order = sys.stdin.readline().strip().split(' ')
# print group, order
n = 5
group = [1, 7, 3, 7, 9]
m = 4
order = [1, 8, 25, 11]
for i in range(int(m)):
    sum = 0
    k = 0
    while order[i] > sum and k <= n-1:
        sum += group[k]
        k += 1
    print k

