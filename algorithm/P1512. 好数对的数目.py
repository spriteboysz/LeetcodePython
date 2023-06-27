#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-25 22:40:32
LastEditTime: 2022-01-25 22:41:55
Description:
FilePath: 1512.好数对的数目.py
"""
#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
# @lc code=end
