#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-27 00:06:40
LastEditTime: 2022-01-27 00:08:16
Description:
FilePath: 1071.字符串的最大公因子.py
"""
#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 字符串的最大公因子
#

# @lc code=start
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            return str1[:gcd(len(str1), len(str2))]
        else:
            return ""
# @lc code=end
