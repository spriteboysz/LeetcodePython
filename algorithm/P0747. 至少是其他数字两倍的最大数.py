#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-16 23:12:18
LastEditTime: 2022-01-16 23:23:38
Description: 
FilePath: 747.至少是其他数字两倍的最大数.py
'''
#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            maximum, b = sorted(nums, reverse=True)[0:2]
            if maximum >= b * 2:
                return nums.index(maximum)
            else:
                max()
                return -1

# @lc code=end


s = Solution()
print(s.dominantIndex([1, 2, 3, 4]))
