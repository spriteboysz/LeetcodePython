#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-26 23:35:11
LastEditTime: 2022-01-26 23:37:24
Description:
FilePath: 1317.将整数转换为两个无零整数的和.py
"""
#
# @lc app=leetcode.cn id=1317 lang=python3
#
# [1317] 将整数转换为两个无零整数的和
#

# @lc code=start
from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if str(i).count("0") == 0 and str(n - i).count("0") == 0:
                return [i, n - i]
# @lc code=end
