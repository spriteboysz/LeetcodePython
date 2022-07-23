#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-21 23:30:18
LastEditTime: 2022-04-21 23:30:37
Description: 
FilePath: 779.第k个语法符号.py
"""
#
# @lc app=leetcode.cn id=779 lang=python3
#
# [779] 第K个语法符号
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if k % 2:
            return self.kthGrammar(n - 1, (k + 1) / 2)
        else:
            return abs(self.kthGrammar(n - 1, k / 2) - 1)


# @lc code=end
