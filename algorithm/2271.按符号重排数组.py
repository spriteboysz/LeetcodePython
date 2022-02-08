#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-08 22:03:43
LastEditTime: 2022-02-08 22:06:50
Description: 
FilePath: 2271.按符号重排数组.py
'''
#
# @lc app=leetcode.cn id=2271 lang=python3
#
# [2149] 按符号重排数组
#

# @lc code=start
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = [], []
        for num in nums:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)
        sequence = []
        for p, n in zip(positive, negative):
            sequence.extend([p, n])
        return sequence
# @lc code=end
