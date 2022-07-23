#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-27 23:14:51
LastEditTime: 2022-01-27 23:17:32
Description: 
FilePath: 1539.第-k-个缺失的正整数.py
'''
#
# @lc app=leetcode.cn id=1539 lang=python3
#
# [1539] 第 k 个缺失的正整数
#

# @lc code=start
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(1, 2002):
            if i not in arr:
                k -= 1
            if k == 0:
                return i
# @lc code=end
