#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-01 21:40:42
LastEditTime: 2022-02-01 21:41:09
Description:
FilePath: 453.最小操作次数使数组元素相等.py
"""
#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小操作次数使数组元素相等
#

# @lc code=start
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            return sum(nums) - len(nums) * min(nums)
# @lc code=end
