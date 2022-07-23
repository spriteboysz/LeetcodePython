#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 16:02:49
LastEditTime: 2022-02-04 16:05:10
Description: 
FilePath: 2269.元素计数.py
'''
#
# @lc app=leetcode.cn id=2269 lang=python3
#
# [2148] 元素计数
#

# @lc code=start
from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        return max(0, len(nums) - nums.count(min(nums)) - nums.count(max(nums)))
# @lc code=end
