#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-24 22:09
FileName: algorithm/P2717. 半有序排列.py
Description: 
"""
from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        index1, index2, n = -1, -1, len(nums)
        for i, num in enumerate(nums):
            if num == 1:
                index1 = i
            if num == n:
                index2 = i
        diff = index1 + n - 1 - index2

        return diff if index1 < index2 else diff - 1


if __name__ == '__main__':
    print(Solution().semiOrderedPermutation(nums=[2, 1, 4, 3]))
