#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-20 22:01:31
LastEditTime: 2022-03-20 22:08:39
Description: 
FilePath: 216.组合总和-iii.py
"""
#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

from itertools import combinations
# @lc code=start
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combination = []
        for item in combinations(range(1, 10), k):
            if sum(item) == n:
                combination.append(list(item))
        return combination


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.combinationSum3(3, 7)
    print(ans)
    ans = solution.combinationSum3(3, 9)
    print(ans)
    ans = solution.combinationSum3(4, 1)
    print(ans)
    ans = solution.combinationSum3(9, 45)
    print(ans)
