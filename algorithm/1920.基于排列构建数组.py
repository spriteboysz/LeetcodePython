#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-22 23:50:16
LastEditTime: 2022-01-22 23:51:43
Description: 
FilePath: 1920.基于排列构建数组.py
'''
#
# @lc app=leetcode.cn id=1920 lang=python3
#
# [1920] 基于排列构建数组
#

# @lc code=start
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]
# @lc code=end
