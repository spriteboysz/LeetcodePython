#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-21 23:21:30
LastEditTime: 2022-05-21 23:25:04
Description: 
FilePath: 剑指 Offer II 084. 含有重复元素集合的全排列 .py
"""

from typing import List
from itertools import permutations


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permute = set()
        for item in permutations(nums):
            permute.add(item)

        return list(map(list, permute))


if __name__ == "__main__":
    solution = Solution()
    ans = solution.permuteUnique([1, 1, 2])
    print(ans)
