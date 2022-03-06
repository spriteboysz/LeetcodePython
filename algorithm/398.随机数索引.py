#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-06 11:25:19
LastEditTime: 2022-03-06 11:29:39
Description: 
FilePath: 398.随机数索引.py
"""
#
# @lc app=leetcode.cn id=398 lang=python3
#
# [398] 随机数索引
#

# @lc code=start
from typing import List
from random import choice
from collections import defaultdict


class Solution:
    def __init__(self, nums: List[int]):
        self.numindex = defaultdict(list)
        for i, num in enumerate(nums):
            self.numindex[num].append(i)

    def pick(self, target: int) -> int:
        return choice(self.numindex[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end
