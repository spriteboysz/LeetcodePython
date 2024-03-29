#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-03 22:20:11
LastEditTime: 2022-02-15 21:58:32
Description:
FilePath: 303.区域和检索-数组不可变.py
"""
#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
