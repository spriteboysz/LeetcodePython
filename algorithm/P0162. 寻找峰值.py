#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-26 14:10:24
LastEditTime: 2022-02-26 14:12:28
Description: 
FilePath: 162.寻找峰值.py
"""
#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

from math import inf
# @lc code=start
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-inf] + nums + [-inf]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i - 1
        return -1


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findPeakElement([1, 2, 3, 1])
    print(ans)
    ans = solution.findPeakElement([1, 2, 1, 3, 5, 6, 4])
    print(ans)
