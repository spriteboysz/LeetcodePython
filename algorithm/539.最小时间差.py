#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-11 22:41:53
LastEditTime: 2022-02-11 22:56:36
Description: 
FilePath: 539.最小时间差.py
'''
#
# @lc app=leetcode.cn id=539 lang=python3
#
# [539] 最小时间差
#

# @lc code=start
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) == len(set(timePoints)):
            return 0
        else:
            time = [0] * (24 * 60 + 1)
            for timepoint in timePoints:
                hour, minitue = map(int, timepoint.split(":"))
                time[hour * 60 + minitue] = 1
            print(time)
# @lc code=end



