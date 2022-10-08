#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-21 21:59:11
LastEditTime: 2022-01-21 22:00:00
Description: 
FilePath: 2124.检查是否所有-a-都在-b-之前.py
'''
#
# @lc app=leetcode.cn id=2124 lang=python3
#
# [2124] 检查是否所有 A 都在 B 之前
#

# @lc code=start
class Solution:
    def checkString(self, s: str) -> bool:
        return "ba" not in s
# @lc code=end

