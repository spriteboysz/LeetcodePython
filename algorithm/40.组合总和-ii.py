#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-20 22:44:09
LastEditTime: 2022-03-20 22:51:41
Description: 
FilePath: 40.组合总和-ii.py
"""
#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from typing import List
from itertools import combinations


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = set()
        for i in range(1, target // min(candidates) + 1):
            for item in combinations(candidates, i):
                if sum(item) == target:
                    combination.add(tuple(sorted(item)))
        return list(map(list, combination))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
    print(ans)
    ans = solution.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5)
    print(ans)
