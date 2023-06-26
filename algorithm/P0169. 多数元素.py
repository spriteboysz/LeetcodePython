#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-01 21:45:01
LastEditTime: 2022-02-01 21:49:06
Description:
FilePath: 169.多数元素.py
"""
#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = []
        for item in list(set(nums)):
            count.append(nums.count(item))
        return list(set(nums))[count.index(max(count))]
# @lc code=end
