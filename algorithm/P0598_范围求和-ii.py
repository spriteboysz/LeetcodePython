#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-03 23:43:23
LastEditTime: 2022-02-03 23:50:03
Description: 
FilePath: 598.范围求和-ii.py
'''
#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#

# @lc code=start
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        rows, columns = [m], [n]
        for row, column in ops:
            rows.append(row)
            columns.append(column)
        return min(rows) * min(columns)


# @lc code=end
