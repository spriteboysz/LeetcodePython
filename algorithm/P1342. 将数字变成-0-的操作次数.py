#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-26 23:05:37
LastEditTime: 2022-01-26 23:07:27
Description:
FilePath: 1342.将数字变成-0-的操作次数.py
"""
#
# @lc app=leetcode.cn id=1342 lang=python3
#
# [1342] 将数字变成 0 的操作次数
#

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            count += 1
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
        return count
# @lc code=end
