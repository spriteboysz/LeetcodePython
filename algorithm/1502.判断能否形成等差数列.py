#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-04 23:25:46
Description: 
FilePath: 1502.判断能否形成等差数列.py
'''
#
# @lc app=leetcode.cn id=1502 lang=python3
#
# [1502] 判断能否形成等差数列
#

# @lc code=start
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        lst = sorted(arr)
        minus = lst[1] - lst[0]
        for i in range(1, len(lst) - 1):
            if lst[i + 1] - lst[i] != minus:
                return False
        return True
# @lc code=end
