#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-11 23:18:55
LastEditTime: 2022-02-11 23:31:48
Description:
FilePath: 1726.同积元组.py
"""
#
# @lc app=leetcode.cn id=1726 lang=python3
#
# [1726] 同积元组
#

from collections import defaultdict
# @lc code=start
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product = defaultdict(int)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                product[nums[i] * nums[j]] += 1
        count = 0
        for item in filter(lambda el: el > 1, product.values()):
            count += item * (item - 1)
        return count * 4

# @lc code=end
