#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-22 16:07
LastEditTime: 2022-05-22 16:07
Description:
FilePath: 剑指 Offer II 079. 所有子集.py.py
"""

from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        for i in range(len(nums) + 1):
            subset.extend(list(combinations(nums, i)))
        return list(map(list, subset))


if __name__ == '__main__':
    solution = Solution()
    ans = solution.subsets([1, 2, 3])
    print(ans)
