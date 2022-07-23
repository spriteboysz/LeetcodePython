#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-28 22:24:38
LastEditTime: 2022-01-28 22:25:26
Description: 
FilePath: 852.山脉数组的峰顶索引.py
'''
#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))
# @lc code=end
