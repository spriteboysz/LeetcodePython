#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-02 21:52:31
LastEditTime: 2022-02-02 22:03:14
Description:
FilePath: 1217.玩筹码.py
"""
#
# @lc app=leetcode.cn id=1217 lang=python3
#
# [1217] 玩筹码
#

# @lc code=start
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = len(list(filter(lambda el: el % 2, position)))
        return min(odd, len(position) - odd)

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.minCostToMoveChips([1, 2, 3]))
    print(s.minCostToMoveChips([2, 2, 2, 3, 3]))
    print(s.minCostToMoveChips([1, 1000000000]))
