#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-09 22:44:53
LastEditTime: 2022-04-09 22:46:21
Description: 
FilePath: 455.分发饼干.py
"""
#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        i, count = 0, 0
        for v in g:
            if i >= len(s):
                break
            elif s[i] >= v:
                count += 1  # 大孩子的需求无论是否满足，都要看下一个孩子的需求
                i += 1
        return count


# @lc code=end
