#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-09-27 23:36:40
Description: 找到所有数组中消失的数字
FilePath: 448.找到所有数组中消失的数字.py
"""
#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ret = [0] * (length + 1)
        for i in range(length):
            ret[nums[i]] += 1

        for j in range(length, 0, -1):
            if ret[j] == 0:
                ret[j] = j
            else:
                del ret[j]
        del ret[0]

        return ret
# @lc code=end

