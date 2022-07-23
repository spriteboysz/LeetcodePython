#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-22 22:02:46
LastEditTime: 2022-04-22 22:05:41
Description: 
FilePath: 498.对角线遍历.py
"""
#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#

# @lc code=start
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m, flag = len(mat), len(mat[0]), 0
        diagonal = []

        for k in range(0, m + n - 1):
            if flag:
                for i in range(max(0, k - m + 1), min(k, n - 1) + 1):
                    diagonal.append(mat[i][k - i])
                flag = 0
            else:
                for i in range(min(k, n - 1), max(0, k - m + 1) - 1, -1):
                    diagonal.append(mat[i][k - i])
                flag = 1

        return diagonal


# @lc code=end
