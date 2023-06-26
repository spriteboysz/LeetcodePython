#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-19 23:20:06
LastEditTime: 2022-01-19 23:22:48
Description:
FilePath: 961.在长度-2-n-的数组中找出重复-n-次的元素.py
"""
#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 在长度 2N 的数组中找出重复 N 次的元素
#

# @lc code=start
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return (sum(nums) - sum(set(nums))) // (len(nums) // 2 - 1)
# @lc code=end
