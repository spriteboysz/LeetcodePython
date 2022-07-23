#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-25 23:00:23
LastEditTime: 2022-01-25 23:04:40
Description: 
FilePath: 1470.重新排列数组.py
'''
#
# @lc app=leetcode.cn id=1470 lang=python3
#
# [1470] 重新排列数组
#

# @lc code=start
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num = []
        for x, y in zip(nums[:n], nums[n:]):
            num.extend([x, y])
        return num

# @lc code=end
