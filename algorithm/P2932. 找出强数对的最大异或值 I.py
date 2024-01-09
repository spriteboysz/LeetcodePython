#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-04 23:22
FileName: algorithm
Description:P2932. 找出强数对的最大异或值 I.py 
"""
from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maximum = 0
        for num1 in nums:
            for num2 in nums:
                if abs(num1 - num2) <= min(num1, num2):
                    maximum = max(maximum, num1 ^ num2)
        return maximum


if __name__ == '__main__':
    print(Solution().maximumStrongPairXor(nums=[1, 2, 3, 4, 5]))
