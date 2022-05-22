#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-22 15:50
LastEditTime: 2022-05-22 15:50
Description:
FilePath: 剑指 Offer II 082. 含有重复元素集合的组合.py.py
"""

from typing import List
from itertools import combinations


class Solution:
    def combinationSum2(self,
                        candidates: List[int],
                        target: int) -> List[List[int]]:
        combination = set()
        for i in range(1, len(candidates) + 1):
            for item in combinations(candidates, i):
                if sum(item) == target:
                    combination.add(tuple(sorted(list(item))))
        return list(map(list, combination))


if __name__ == '__main__':
    solution = Solution()
    ans = solution.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
    print(ans)
