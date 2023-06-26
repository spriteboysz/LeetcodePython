#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-23 16:55:30
LastEditTime: 2022-01-23 16:58:30
Description:
FilePath: 1805.字符串中不同整数的数目.py
"""
#
# @lc app=leetcode.cn id=1805 lang=python3
#
# [1805] 字符串中不同整数的数目
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = ""
        for item in word:
            if item in ascii_lowercase:
                nums += " "
            else:
                nums += item
        return len(set(map(int, nums.strip().split())))
# @lc code=end
