# -*- coding:utf-8 -*-


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        arr = [1]
        m2 = 0
        m3 = 0
        m5 = 0
        for i in range(index):
            min_num = min(arr[m2]*2, arr[m3]*3, arr[m5]*5)
            arr.append(min_num)
            if min_num == arr[m2]*2:
                m2 += 1
            if min_num == arr[m3]*3:
                m3 += 1
            if min_num == arr[m5]*5:
                m5 += 1
        return arr[index - 1]


s = Solution()
print(s.GetUglyNumber_Solution(0))