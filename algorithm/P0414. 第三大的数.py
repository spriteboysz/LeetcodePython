#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-09-27 23:16:45
Description: 第三大的数
FilePath: 414.第三大的数.py
"""
#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        snum = sorted(list(set(nums)), reverse=True)
        if len(snum) >= 3:
            return snum[2]
        else:
            return max(snum)
            
# @lc code=end

