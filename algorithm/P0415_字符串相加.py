#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-27 23:21:04
Description: 字符串相加
FilePath: 415.字符串相加.py
'''
#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))

# @lc code=end
