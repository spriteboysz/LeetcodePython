#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-23 22:42:03
LastEditTime: 2022-01-23 22:43:01
Description:
FilePath: 1672.最富有客户的资产总量.py
"""
#
# @lc app=leetcode.cn id=1672 lang=python3
#
# [1672] 最富有客户的资产总量
#

# @lc code=start
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(lambda el: sum(el), accounts))
# @lc code=end
