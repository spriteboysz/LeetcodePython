#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-03 23:35:13
LastEditTime: 2022-02-03 23:38:50
Description:
FilePath: 521.最长特殊序列-ⅰ.py
"""


#
# @lc app=leetcode.cn id=521 lang=python3
#
# [521] 最长特殊序列 Ⅰ
#

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return max(len(a), len(b))
        else:
            if a == b:
                return -1
            else:
                return len(a)
# @lc code=end
