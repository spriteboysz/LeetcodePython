#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-25 23:14:46
LastEditTime: 2022-01-25 23:16:11
Description:
FilePath: 1446.连续字符.py
"""
#
# @lc app=leetcode.cn id=1446 lang=python3
#
# [1446] 连续字符
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        count = [1] * len(s)
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                count[i] = count[i - 1] + 1
        return max(count)
# @lc code=end
