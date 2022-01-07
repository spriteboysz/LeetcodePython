#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-04 23:09:14
Description: 
FilePath: 1662.检查两个字符串数组是否相等.py
'''
#
# @lc app=leetcode.cn id=1662 lang=python3
#
# [1662] 检查两个字符串数组是否相等
#

# @lc code=start
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
# @lc code=end

