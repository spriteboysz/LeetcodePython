#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 14:05:34
LastEditTime: 2022-02-04 14:08:13
Description: 
FilePath: 100331.0-～n-1-中缺失的数字.py
'''
#
# @lc app=leetcode.cn id=100331 lang=python3
#
# [剑指 Offer 53 - II] 0～n-1中缺失的数字
#

# @lc code=start
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
# @lc code=end
