#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-19 23:13:20
LastEditTime: 2022-02-19 23:16:27
Description: 
FilePath: 274.h-指数.py
"""
#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations + [0], reverse=True)
        for i, citation in enumerate(citations):
            if i + 1 > citation:
                return i


# @lc code=end
