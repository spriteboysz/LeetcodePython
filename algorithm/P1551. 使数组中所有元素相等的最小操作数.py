#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-15 22:20:28
LastEditTime: 2022-02-15 22:22:45
Description:
FilePath: 1551.使数组中所有元素相等的最小操作数.py
"""
#
# @lc app=leetcode.cn id=1551 lang=python3
#
# [1551] 使数组中所有元素相等的最小操作数
#

# @lc code=start
class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return (n * n) // 4
        else:
            return (n * n - 1) // 4
# @lc code=end
