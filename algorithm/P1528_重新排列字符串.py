#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-25 22:29:59
LastEditTime: 2022-01-25 22:32:43
Description: 
FilePath: 1528.重新排列字符串.py
'''
#
# @lc app=leetcode.cn id=1528 lang=python3
#
# [1528] 重新排列字符串
#

# @lc code=start
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s2 = ""
        for i in range(len(s)):
            s2 += s[indices.index(i)]
        return s2

# @lc code=end
