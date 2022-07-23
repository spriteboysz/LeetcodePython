#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-09 20:14:05
LastEditTime: 2022-04-09 20:16:15
Description: 
FilePath: 1985.找出数组中的第-k-大整数.py
"""
#
# @lc app=leetcode.cn id=1985 lang=python3
#
# [1985] 找出数组中的第 K 大整数
#

# @lc code=start
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return sorted(nums, key=int, reverse=True)[k - 1]
