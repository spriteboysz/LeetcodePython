#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-23 18:01:42
LastEditTime: 2022-01-23 18:07:41
Description: 
FilePath: 1748.唯一元素的和.py
'''
#
# @lc app=leetcode.cn id=1748 lang=python3
#
# [1748] 唯一元素的和
#

# @lc code=start
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = map(lambda el: nums.count(el) == 1, nums)
        sum = 0
        for n, c in zip(nums, count):
            sum += n * int(c)
        return sum
# @lc code=end
