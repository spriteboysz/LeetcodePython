#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-27 00:02:03
LastEditTime: 2022-01-27 00:06:05
Description: 
FilePath: 1078.bigram-分词.py
'''
#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#

# @lc code=start
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.strip().split()
        third = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                third.append(words[i + 2])
        return third


# @lc code=end
