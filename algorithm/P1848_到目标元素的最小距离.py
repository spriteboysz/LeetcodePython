#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-30 22:06:12
LastEditTime: 2022-01-30 22:10:33
Description: 
FilePath: 1848.到目标元素的最小距离.py
'''
#
# @lc app=leetcode.cn id=1848 lang=python3
#
# [1848] 到目标元素的最小距离
#

# @lc code=start
from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        position = []
        for i, item in enumerate(nums):
            if item == target:
                position.append(i)
        return min(map(lambda el: abs(el - start), position))
# @lc code=end
