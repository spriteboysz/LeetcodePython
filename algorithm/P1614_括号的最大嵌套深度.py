#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-24 23:34:32
LastEditTime: 2022-01-24 23:37:23
Description: 
FilePath: 1614.括号的最大嵌套深度.py
'''
#
# @lc app=leetcode.cn id=1614 lang=python3
#
# [1614] 括号的最大嵌套深度
#

# @lc code=start


class Solution:
    def maxDepth(self, s: str) -> int:
        maximum, depth = 0, 0
        for item in s:
            if item == "(":
                depth += 1
            elif item == ")":
                depth -= 1
            if depth > maximum:
                maximum = depth
        return maximum
# @lc code=end
