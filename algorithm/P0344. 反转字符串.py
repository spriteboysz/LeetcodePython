#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-09-27 22:56:48
Description: 反转字符串
FilePath: 344.反转字符串.py
"""
#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = []
        for item in s:
            l.append(item)

        for i in range(0, len(s)):
            s[i] = l[len(s) - 1 - i]
# @lc code=end
