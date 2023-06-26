#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-10-05 14:02:52
Description:
FilePath: 1491.去掉最低工资和最高工资后的工资平均值.py
"""
#
# @lc app=leetcode.cn id=1491 lang=python3
#
# [1491] 去掉最低工资和最高工资后的工资平均值
#

# @lc code=start
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
# @lc code=end
