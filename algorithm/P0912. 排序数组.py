#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-11 23:57:15
LastEditTime: 2022-02-11 23:57:39
Description:
FilePath: 912.排序数组.py
"""
#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
# @lc code=end
