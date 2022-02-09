#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-09 21:39:35
LastEditTime: 2022-02-09 21:42:18
Description: 
FilePath: 1877.数组中最大数对和的最小值.py
'''
#
# @lc app=leetcode.cn id=1877 lang=python3
#
# [1877] 数组中最大数对和的最小值
#

# @lc code=start
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maximum = 0
        for i in range(len(nums)//2):
            maximum = max(maximum, nums[i] + nums[-(i + 1)])
        return maximum
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.minPairSum([3, 5, 4, 2, 4, 6]))
