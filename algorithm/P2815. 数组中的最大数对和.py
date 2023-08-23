#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-22 23:37
FileName: algorithm
Description:P2815. 数组中的最大数对和.py 
"""
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maximum, n = -1, len(nums)
        for i in range(0, n):
            for j in range(i + 1, n):
                if max(list(str(nums[i]))) == max(list(str(nums[j]))):
                    maximum = max(maximum, nums[i] + nums[j])
        return maximum


if __name__ == '__main__':
    print(Solution().maxSum(nums=[51, 71, 17, 24, 42]))
