#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 22:36:22
LastEditTime: 2022-02-04 22:38:28
Description: 
FilePath: 100301.最小的k个数.py
'''
#
# @lc app=leetcode.cn id=100301 lang=python3
#
# [剑指 Offer 40] 最小的k个数
#

# @lc code=start
from typing import List
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]
# @lc code=end

