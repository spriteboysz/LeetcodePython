#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 14:13:06
LastEditTime: 2022-02-04 14:14:12
Description: 
FilePath: 100322.和为s的两个数字.py
'''
#
# @lc app=leetcode.cn id=100322 lang=python3
#
# [剑指 Offer 57] 和为s的两个数字
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            if target - num in nums:
                return [num, target - num]
            
# @lc code=end

