#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-05 15:58:51
LastEditTime: 2022-03-05 16:04:11
Description: 
FilePath: 1276.不浪费原料的汉堡制作方案.py
"""
#
# @lc app=leetcode.cn id=1276 lang=python3
#
# [1276] 不浪费原料的汉堡制作方案
#

# @lc code=start
from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # 4 * x + y = tomatoSlices
        # 2 * x + y = cheeseSlices
        if tomatoSlices % 2 == 1:
            return []
        x = tomatoSlices // 2 -  cheeseSlices
        y = 2 * cheeseSlices - tomatoSlices // 2
        if x < 0 or y < 0:
            return []
        return [x, y]


# @lc code=end
