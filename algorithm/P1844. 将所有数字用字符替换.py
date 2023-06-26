#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-23 16:48:56
LastEditTime: 2022-01-23 16:53:03
Description:
FilePath: 1844.将所有数字用字符替换.py
"""
#
# @lc app=leetcode.cn id=1844 lang=python3
#
# [1844] 将所有数字用字符替换
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def replaceDigits(self, s: str) -> str:
        s2 = ""
        for i, letter in enumerate(s):
            if i % 2 == 0:
                s2 += letter
            else:
                s2 += ascii_lowercase[ascii_lowercase.index(
                    s[i - 1]) + int(letter)]
        return s2
# @lc code=end
