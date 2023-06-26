#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-06 16:19:50
LastEditTime: 2022-02-06 16:23:02
Description:
FilePath: 703.数据流中的第-k-大元素.py
"""
#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#

# @lc code=start
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end
