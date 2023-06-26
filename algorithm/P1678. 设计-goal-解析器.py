#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-23 22:40:00
LastEditTime: 2022-01-23 22:41:06
Description:
FilePath: 1678.设计-goal-解析器.py
"""
#
# @lc app=leetcode.cn id=1678 lang=python3
#
# [1678] 设计 Goal 解析器
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")
# @lc code=end
