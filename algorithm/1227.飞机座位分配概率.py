#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-10 22:13:08
LastEditTime: 2022-02-10 22:14:18
Description: 
FilePath: 1227.飞机座位分配概率.py
'''
#
# @lc app=leetcode.cn id=1227 lang=python3
#
# [1227] 飞机座位分配概率
#

# @lc code=start
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1.0 / n
        else:
            return 0.5 / 1.0
# @lc code=end

