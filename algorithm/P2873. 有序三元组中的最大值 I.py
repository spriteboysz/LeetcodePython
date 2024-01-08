#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-08 22:57
FileName: algorithm
Description:P2873. 有序三元组中的最大值 I.py 
"""
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maximum = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    maximum = max(maximum, (nums[i] - nums[j]) * nums[k])
        return maximum


if __name__ == '__main__':
    print(Solution().maximumTripletValue(nums=[12, 6, 1, 2, 7]))
