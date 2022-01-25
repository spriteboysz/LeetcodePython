#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-25 22:52:57
LastEditTime: 2022-01-25 22:59:34
Description: 
FilePath: 1480.一维数组的动态和.py
'''
#
# @lc app=leetcode.cn id=1480 lang=python3
#
# [1480] 一维数组的动态和
#

# @lc code=start
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running, cur = [], 0
        for item in nums:
            cur += item
            running.append(cur)
        return running
# @lc code=end
