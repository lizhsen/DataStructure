# -*- coding:utf-8 -*-


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        ori_str = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                   'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        ori_index = [0] *len(ori_str)
        result = []
        strs = s
        for i in strs:
            for j in range(len(ori_str)):
                if str.lower(i) == ori_str[j]:
                    ori_index[j] += 1
        for k in range(len(ori_str)):
            if ori_index[k] == 1:
                result.append(ori_str[k])
        for i in range(len(strs)):
            if str.lower(strs[i]) in result:
                return i
