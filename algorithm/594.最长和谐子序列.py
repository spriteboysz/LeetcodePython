#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-13 23:38:45
LastEditTime: 2022-01-13 23:55:25
Description: 
FilePath: 594.最长和谐子序列.py
'''
#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {item: nums.count(item) for item in set(nums)}
        maximum = 0
        key = list(dic.keys())
        for i in range(len(key) - 1):
            for j in range(i + 1, len(key)):
                if abs(key[i] - key[j]) == 1:
                    maximum = max(maximum, dic[key[i]] + dic[key[j]])
        return maximum
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
