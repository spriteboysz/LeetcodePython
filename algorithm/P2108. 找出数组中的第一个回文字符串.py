#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-21 22:09:44
LastEditTime: 2022-01-21 22:10:55
Description:
FilePath: 2108.找出数组中的第一个回文字符串.py
"""
#
# @lc app=leetcode.cn id=2108 lang=python3
#
# [2108] 找出数组中的第一个回文字符串
#

# @lc code=start
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""
# @lc code=end
