#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-24 23:53
FileName: algorithm/P2441. 与对应负数同时存在的最大正整数.py
Description: 
"""
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        sets = set(nums)
        for num in sorted(nums, reverse=True):
            if -num in sets:
                return num
        return -1


if __name__ == '__main__':
    solution = Solution().findMaxK([-1, 10, 6, 7, -7, 1])
    print(solution)
    solution = Solution().findMaxK([-10, 8, 6, 7, -2, -3])
    print(solution)
