#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-22 23:52:37
LastEditTime: 2022-01-22 23:54:32
Description:
FilePath: 1913.两个数对之间的最大乘积差.py
"""
#
# @lc app=leetcode.cn id=1913 lang=python3
#
# [1913] 两个数对之间的最大乘积差
#

# @lc code=start
from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a, d = max(nums), min(nums)
        nums.remove(a)
        nums.remove(d)
        b, c = max(nums), min(nums)
        return a * b - c * d
# @lc code=end
