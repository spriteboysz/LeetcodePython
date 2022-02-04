#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 23:00:13
LastEditTime: 2022-02-04 23:01:07
Description: 
FilePath: 100240.魔术索引.py
'''
#
# @lc app=leetcode.cn id=100240 lang=python3
#
# [面试题 08.03] 魔术索引
#

# @lc code=start
from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i == num:
                return i
        return -1
# @lc code=end
