#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-30 00:03:49
LastEditTime: 2022-03-30 00:04:44
Description: 
FilePath: 2185.统计包含给定前缀的字符串.py
"""
#
# @lc app=leetcode.cn id=2185 lang=python3
#
# [2185] 统计包含给定前缀的字符串
#

# @lc code=start
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count


# @lc code=end
