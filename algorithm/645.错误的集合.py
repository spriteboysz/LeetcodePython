#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-10 22:56:17
LastEditTime: 2022-01-10 23:04:15
Description: 
FilePath: 645.错误的集合.py
'''
#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total = len(nums) * (1 + len(nums)) // 2
        lose = total - sum(set(nums))
        repeat = sum(nums) - total + lose
        return [repeat, lose]

# @lc code=end
