#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-08 23:01
FileName: algorithm
Description:P2869. 收集元素的最少操作次数.py 
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        digits = [False] * k
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] - 1 < k:
                digits[nums[i] - 1] = True
            if all(digits):
                return len(nums) - i


if __name__ == '__main__':
    print(Solution().minOperations(nums=[3, 2, 5, 3, 1], k=3))
