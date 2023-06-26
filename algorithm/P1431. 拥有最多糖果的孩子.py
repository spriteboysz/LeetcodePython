#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-25 23:25:36
LastEditTime: 2022-01-25 23:27:20
Description:
FilePath: 1431.拥有最多糖果的孩子.py
"""
#
# @lc app=leetcode.cn id=1431 lang=python3
#
# [1431] 拥有最多糖果的孩子
#

# @lc code=start
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        return list(map(lambda el: el + extraCandies >= maximum, candies))
# @lc code=end
