#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-07 21:56:55
LastEditTime: 2022-02-07 21:59:44
Description:
FilePath: 2144.打折购买糖果的最小开销.py
"""
#
# @lc app=leetcode.cn id=2144 lang=python3
#
# [2144] 打折购买糖果的最小开销
#

# @lc code=start
from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        return sum(cost) - sum(cost[2::3])
# @lc code=end
