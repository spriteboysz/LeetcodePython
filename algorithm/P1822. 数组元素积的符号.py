#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-10-04 22:31:54
Description:
FilePath: 1822.数组元素积的符号.py
"""
#
# @lc app=leetcode.cn id=1822 lang=python3
#
# [1822] 数组元素积的符号
#

# @lc code=start
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = 0
        for item in nums:
            if item == 0:
                return 0
            elif item < 0:
                count += 1

        return 1 if count % 2 == 0 else -1                
        
    
# @lc code=end

