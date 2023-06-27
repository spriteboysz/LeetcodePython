#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-09-27 23:23:36
Description: 字符串中的单词数
FilePath: 434.字符串中的单词数.py
"""


#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.strip().split())
# @lc code=end
