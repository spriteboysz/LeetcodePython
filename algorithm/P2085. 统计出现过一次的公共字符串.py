#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-21 23:07:23
LastEditTime: 2022-01-21 23:09:56
Description:
FilePath: 2085.统计出现过一次的公共字符串.py
"""
#
# @lc app=leetcode.cn id=2085 lang=python3
#
# [2085] 统计出现过一次的公共字符串
#

# @lc code=start
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        common = list(set(words1) & set(words2))
        count = 0
        for word in common:
            if words1.count(word) == words2.count(word) == 1:
                count += 1
        return count
# @lc code=end
