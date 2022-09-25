#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-04 15:59:53
LastEditTime: 2022-02-04 16:00:52
Description:
FilePath: 100107.猜数字.py
"""
#
# @lc app=leetcode.cn id=100107 lang=python3
#
# [LCP 01] 猜数字
#

# @lc code=start
from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        count = 0
        for g, a in zip(guess, answer):
            if g == a:
                count += 1
        return count
# @lc code=end
