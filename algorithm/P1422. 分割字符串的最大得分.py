#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-25 23:28:32
LastEditTime: 2022-01-25 23:35:25
Description:
FilePath: 1422.分割字符串的最大得分.py
"""
#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 分割字符串的最大得分
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        maximum, cur = 0, 0
        for i in range(1, len(s)):
            cur = s[:i].count("0") + s[i:].count("1")
            if cur > maximum:
                maximum = cur
        return maximum
# @lc code=end

