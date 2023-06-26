#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-26 23:56:52
LastEditTime: 2022-01-26 23:58:40
Description:
FilePath: 1295.统计位数为偶数的数字.py
"""
#
# @lc app=leetcode.cn id=1295 lang=python3
#
# [1295] 统计位数为偶数的数字
#

# @lc code=start
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(lambda el: len(str(el)) % 2 == 0, nums)))
# @lc code=end
