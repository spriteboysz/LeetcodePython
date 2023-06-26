#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-25 23:51:09
LastEditTime: 2022-01-25 23:57:16
Description:
FilePath: 1408.数组中的字符串匹配.py
"""
#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#

# @lc code=start
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len)
        substring = set()
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    substring.add(words[i])
        return list(substring)

# @lc code=end
