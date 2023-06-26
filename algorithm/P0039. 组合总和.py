#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-20 22:34:07
LastEditTime: 2022-03-20 22:38:39
Description: 
FilePath: 39.组合总和.py
"""
#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

from itertools import combinations_with_replacement
# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = []
        for i in range(1, target // min(candidates) + 1):
            for item in combinations_with_replacement(candidates, i):
                if sum(item) == target:
                    combination.append(list(item))
        return combination


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.combinationSum([2, 3, 6, 7], 7)
    print(ans)
    ans = solution.combinationSum([2, 3, 5], 8)
    print(ans)
    ans = solution.combinationSum([2], 1)
    print(ans)
