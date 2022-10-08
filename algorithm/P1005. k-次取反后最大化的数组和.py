#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-20 23:09:52
LastEditTime: 2022-01-20 23:35:15
Description: 
FilePath: 1005.k-次取反后最大化的数组和.py
'''
#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

# @lc code=start
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        negative = list(sorted(filter(lambda el: el < 0, nums)))
        positive = list(sorted(filter(lambda el: el >= 0, nums)))
        if k <= len(negative):
            maximum = abs(sum(negative[:k])) + \
                sum(negative[k:]) + sum(positive)
        else:
            if 0 in positive or (k - len(negative)) % 2 == 0:
                maximum = abs(sum(negative)) + sum(positive)
            else:
                maximum = abs(sum(negative)) + sum(positive) - \
                    min(map(abs, nums)) * 2
        return maximum

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.largestSumAfterKNegations([4, 2, 3], 1))
    print(s.largestSumAfterKNegations([3, -1, 0, 2], 6))
    print(s.largestSumAfterKNegations([2, -3, -1, 5, -4], 2))
    print(s.largestSumAfterKNegations([-8, 3, -5, -3, -5, -2], 6))
