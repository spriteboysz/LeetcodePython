#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 14:21:06
LastEditTime: 2022-02-04 14:24:35
Description: 
FilePath: 100291.调整数组顺序使奇数位于偶数前面.py
'''
#
# @lc app=leetcode.cn id=100291 lang=python3
#
# [剑指 Offer 21] 调整数组顺序使奇数位于偶数前面
#

# @lc code=start
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        return list(sorted(nums, key=lambda el: el % 2, reverse=True))
# @lc code=end
