#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-27 23:24:07
LastEditTime: 2022-02-27 23:25:47
Description: 
FilePath: 384.打乱数组.py
"""
#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

import random
from copy import copy
# @lc code=start
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        # temp = copy(self.nums)
        random.shuffle(temp := copy(self.nums))
        return temp


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end
