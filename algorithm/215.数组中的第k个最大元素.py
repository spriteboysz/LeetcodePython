#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-06 21:33:25
LastEditTime: 2022-02-06 21:34:19
Description: 
FilePath: 215.数组中的第k个最大元素.py
'''
#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
# @lc code=end
