#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-27 23:42:38
LastEditTime: 2022-01-27 23:43:52
Description:
FilePath: 1389.按既定顺序创建目标数组.py
"""
#
# @lc app=leetcode.cn id=1389 lang=python3
#
# [1389] 按既定顺序创建目标数组
#

# @lc code=start
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for n, i in zip(nums, index):
            target.insert(i, n)
        return target
# @lc code=end
