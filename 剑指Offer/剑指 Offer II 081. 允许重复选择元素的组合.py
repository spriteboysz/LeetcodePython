#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-22 10:54
LastEditTime: 2022-05-22 10:54
Description:
FilePath: 剑指 Offer II 081. 允许重复选择元素的组合.py.py
"""

from typing import List
from itertools import combinations_with_replacement


class Solution:
    def combinationSum(self,
                       candidates: List[int],
                       target: int) -> List[List[int]]:
        lst = []
        for i in range(1, target // min(candidates) + 1):
            for combination in combinations_with_replacement(candidates, i):
                if sum(combination) == target:
                    lst.append(list(combination))
        return lst


if __name__ == '__main__':
    solution = Solution()
    ans = solution.combinationSum([2, 3, 6, 7], 7)
    print(ans)
    ans = solution.combinationSum([2, 3, 5], 8)
    print(ans)
