#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-26 00:09:37
LastEditTime: 2022-01-26 00:12:22
Description:
FilePath: 1394.找出数组中的幸运数.py
"""
#
# @lc app=leetcode.cn id=1394 lang=python3
#
# [1394] 找出数组中的幸运数
#

# @lc code=start
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for num in sorted(set(arr), reverse=True):
            if arr.count(num) == num:
                return num
        return -1
# @lc code=end
