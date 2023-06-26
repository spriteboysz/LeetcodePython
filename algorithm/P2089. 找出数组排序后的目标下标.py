#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-21 23:04:03
LastEditTime: 2022-01-21 23:06:08
Description:
FilePath: 2089.找出数组排序后的目标下标.py
"""
#
# @lc app=leetcode.cn id=2089 lang=python3
#
# [2089] 找出数组排序后的目标下标
#

# @lc code=start
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        indices = []
        for i, v in enumerate(nums):
            if v == target:
                indices.append(i)
        return indices
# @lc code=end
