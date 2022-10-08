#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-22 22:52:10
LastEditTime: 2022-01-22 22:53:21
Description: 
FilePath: 1967.作为子字符串出现在单词中的字符串数目.py
'''
#
# @lc app=leetcode.cn id=1967 lang=python3
#
# [1967] 作为子字符串出现在单词中的字符串数目
#

# @lc code=start
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count
# @lc code=end
