#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-04-14 23:26:58
LastEditTime: 2022-04-14 23:31:15
Description: 
FilePath: 1402.做菜顺序.py
'''
#
# @lc app=leetcode.cn id=1402 lang=python3
#
# [1402] 做菜顺序
#

# @lc code=start
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        res, total = 0, 0
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total

        return res


# @lc code=end
