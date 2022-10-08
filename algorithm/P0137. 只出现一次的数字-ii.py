#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-09 23:29:02
LastEditTime: 2022-02-09 23:31:49
Description: 
FilePath: 137.只出现一次的数字-ii.py
'''
#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = dict()
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        count = {v: i for i, v in count.items()}
        return count[1]

# @lc code=end
