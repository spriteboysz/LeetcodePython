#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-05 22:38:52
Description: 
FilePath: 977.有序数组的平方.py
'''
#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x * x, nums)))
# @lc code=end
