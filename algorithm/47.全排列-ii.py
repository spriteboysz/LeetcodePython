#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-18 00:06:07
LastEditTime: 2022-02-18 00:06:59
Description: 
FilePath: 47.全排列-ii.py
"""
#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
from typing import List
from itertools import permutations


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(map(lambda el: list(el), set(permutations(nums, len(nums)))))


# @lc code=end
