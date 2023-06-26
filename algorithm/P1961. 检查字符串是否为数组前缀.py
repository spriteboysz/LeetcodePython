#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-22 22:53:50
LastEditTime: 2022-01-22 22:56:15
Description:
FilePath: 1961.检查字符串是否为数组前缀.py
"""
#
# @lc app=leetcode.cn id=1961 lang=python3
#
# [1961] 检查字符串是否为数组前缀
#

# @lc code=start
from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ""
        for word in words:
            prefix += word
            if prefix == s:
                return True
            if len(prefix) > len(s):
                break
        return False
# @lc code=end
