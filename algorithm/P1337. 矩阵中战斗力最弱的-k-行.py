#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-26 23:08:12
LastEditTime: 2022-01-26 23:19:29
Description:
FilePath: 1337.矩阵中战斗力最弱的-k-行.py
"""
#
# @lc app=leetcode.cn id=1337 lang=python3
#
# [1337] 矩阵中战斗力最弱的 K 行
#

from math import inf
# @lc code=start
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        effective = []
        for row in mat:
            effective.append(sum(row))
        weakest = []
        for item in sorted(effective):
            weakest.append(effective.index(item))
            effective[effective.index(item)] = inf
            if len(weakest) == k:
                break
        return weakest
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.kWeakestRows([[1, 1, 0, 0, 0],
                          [1, 1, 1, 1, 0],
                          [1, 0, 0, 0, 0],
                          [1, 1, 0, 0, 0],
                          [1, 1, 1, 1, 1]], 3))
