#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-05 13:53:40
Description: 
FilePath: 1281.整数的各位积和之差.py
'''
#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p, s = 1, 0
        for item in list(str(n)):
            p *= int(item)
            s += int(item)
        return p - s
# @lc code=end
