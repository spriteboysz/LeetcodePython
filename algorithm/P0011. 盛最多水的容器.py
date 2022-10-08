#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-10 14:13:02
LastEditTime: 2022-04-10 14:17:40
Description: 
FilePath: 11.盛最多水的容器.py
"""
#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, area = 0, len(height) - 1, 0
        while left < right:
            if height[left] < height[right]:
                area = max(area, height[left] * (right - left))
                left += 1
            else:
                area = max(area, height[right] * (right - left))
                right -= 1
        return area


# @lc code=end
