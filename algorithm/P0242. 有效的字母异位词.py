#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-14 23:52:23
LastEditTime: 2022-01-15 00:00:12
Description:
FilePath: 242.有效的字母异位词.py
"""
#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = list(map(lambda el: s.count(el), ascii_lowercase))
        tc = list(map(lambda el: t.count(el), ascii_lowercase))
        return sc == tc
# @lc code=end
