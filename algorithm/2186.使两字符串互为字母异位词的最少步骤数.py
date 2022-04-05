#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 16:13:10
LastEditTime: 2022-04-05 16:22:45
Description: 
FilePath: 2186.使两字符串互为字母异位词的最少步骤数.py
"""
#
# @lc app=leetcode.cn id=2186 lang=python3
#
# [2186] 使两字符串互为字母异位词的最少步骤数
#

# @lc code=start
from string import ascii_lowercase as lower


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        alphabet = [0] * 26
        for item in s:
            alphabet[lower.index(item)] += 1
        for item in t:
            alphabet[lower.index(item)] -= 1
        return sum(map(abs, alphabet))


# @lc code=end
