#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-08 22:49
FileName: algorithm
Description:P2903. 找出满足差值条件的下标 I.py 
"""
from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i in range(len(nums) - indexDifference):
            for j in range(i + indexDifference, len(nums)):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]


if __name__ == '__main__':
    print(Solution().findIndices(nums=[5, 1, 4, 1], indexDifference=2, valueDifference=4))
