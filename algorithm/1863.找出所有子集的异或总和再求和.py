#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-15 23:07:20
LastEditTime: 2022-02-15 23:12:06
Description: 
FilePath: 1863.找出所有子集的异或总和再求和.py
'''
#
# @lc app=leetcode.cn id=1863 lang=python3
#
# [1863] 找出所有子集的异或总和再求和
#

# @lc code=start
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = [0]
        for x in nums:
            subsets += [x ^ y for y in subsets]
        return sum(subsets)


# @lc code=end
