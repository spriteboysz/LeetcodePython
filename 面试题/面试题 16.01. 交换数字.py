#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-05 23:22:39
LastEditTime: 2022-02-05 23:23:29
Description:
FilePath: 100258.交换数字.py
"""
#
# @lc app=leetcode.cn id=100258 lang=python3
#
# [面试题 16.01] 交换数字
#

# @lc code=start
from typing import List


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        return numbers[::-1]
# @lc code=end
