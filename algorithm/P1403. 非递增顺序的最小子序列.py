#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-30 23:25:09
LastEditTime: 2022-01-30 23:30:48
Description:
FilePath: 1403.非递增顺序的最小子序列.py
"""
#
# @lc app=leetcode.cn id=1403 lang=python3
#
# [1403] 非递增顺序的最小子序列
#

# @lc code=start
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)
        total = sum(nums)
        for i in range(len(nums)):
            if sum(nums[:i + 1]) > total - sum(nums[:i + 1]):
                return nums[:i + 1]

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.minSubsequence([4, 4, 7, 6, 7]))
    print(s.minSubsequence([6]))
