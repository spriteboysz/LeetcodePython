#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-27 23:44:33
LastEditTime: 2022-01-27 23:46:39
Description: 
FilePath: 1374.生成每种字符都是奇数个的字符串.py
'''
#
# @lc app=leetcode.cn id=1374 lang=python3
#
# [1374] 生成每种字符都是奇数个的字符串
#

# @lc code=start
class Solution:
    def generateTheString(self, n: int) -> str:
        return "a" * n if n % 2 else "a" * (n - 1) + "b"
# @lc code=end
