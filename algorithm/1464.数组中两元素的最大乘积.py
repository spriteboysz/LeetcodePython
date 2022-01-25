#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-25 23:05:38
LastEditTime: 2022-01-25 23:07:01
Description: 
FilePath: 1464.数组中两元素的最大乘积.py
'''
#
# @lc app=leetcode.cn id=1464 lang=python3
#
# [1464] 数组中两元素的最大乘积
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = max(nums)
        nums.remove(maximum)
        return (maximum - 1) * (max(nums) - 1)
# @lc code=end
