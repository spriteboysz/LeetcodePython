#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-20 12:42
FileName: algorithm
Description:P3105. 最长的严格递增或递减子数组.py 
"""
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maximum, n = 1, len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j - 1] > nums[j]:
                    maximum = max(maximum, j - i + 1)
                else:
                    break
            for j in range(i + 1, n):
                if nums[j - 1] < nums[j]:
                    maximum = max(maximum, j - i + 1)
                else:
                    break
        return maximum


if __name__ == '__main__':
    print(Solution().longestMonotonicSubarray(nums=[1, 4, 3, 3, 2]))
