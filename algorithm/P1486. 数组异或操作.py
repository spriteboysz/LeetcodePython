#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-25 22:49:46
LastEditTime: 2022-01-25 22:52:16
Description:
FilePath: 1486.数组异或操作.py
"""
#
# @lc app=leetcode.cn id=1486 lang=python3
#
# [1486] 数组异或操作
#

# @lc code=start
from functools import reduce


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]
        return reduce(lambda a, b: a ^ b, nums)
# @lc code=end
