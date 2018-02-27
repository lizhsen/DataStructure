# -*- coding: UTF-8 -*-


def anagram_solution(s1, s2):
    """
    判断两个字符是否互为变位词
    :param s1:word1
    :param s2:word2
    :return: True or False
    """
    c1 = [0]*26
    c2 = [0]*26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for j in range(len(s2)):
        pos = ord(s2[j]) - ord('a')
        c2[pos] = c2[pos] + 1
    k = 0
    still_ok = True
    while k < 26 and still_ok:
        if c1[k] == c2[k]:
            k += 1
        else:
            still_ok = False
    return still_ok


# print(anagram_solution('apple', 'ppalb'))
"""
找出出现次数最多的数字
"""
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 5]
print (set(test))
print max(set(test), key=test.count)
