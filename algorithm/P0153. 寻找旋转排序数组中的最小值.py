#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-17 17:13:04
LastEditTime: 2022-04-17 17:13:31
Description:
FilePath: 153.寻找旋转排序数组中的最小值.py
"""
#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
# @lc code=end
