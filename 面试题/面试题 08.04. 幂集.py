#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-25 22:32
LastEditTime: 2022-05-25 22:32
Description:
FilePath: 面试题 08.04. 幂集.py
"""

from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [list(item) for i in range(len(nums) + 1)
                for item in combinations(nums, i)]
        # subset = []
        # for i in range(len(nums) + 1):
        #     for item in combinations(nums, i):
        #         subset.append(list(item))
        # return subset


if __name__ == '__main__':
    solution = Solution()
    ans = solution.subsets([1, 2, 3])
    print(ans)
