#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-02 22:05:21
LastEditTime: 2022-02-02 22:11:24
Description:
FilePath: 1089.复写零.py
"""
#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#

# @lc code=start
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index, n = 0, len(arr)
        while index < n:
            if arr[index] == 0:
                arr.insert(index, 0)
                arr.pop()
                index += 2
            else:
                index += 1
# @lc code=end
