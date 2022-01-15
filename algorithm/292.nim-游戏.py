#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-07 23:00:34
LastEditTime: 2022-01-15 21:50:02
Description: 
FilePath: 292.nim-游戏.py
'''
#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        return True if n % 4 else False
# @lc code=end

