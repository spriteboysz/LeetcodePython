#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-08 22:37
FileName: algorithm
Description:P2908. 元素和最小的山形三元组 I.py 
"""
import math
from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        minimum = math.inf
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] > nums[k]:
                        minimum = min(minimum, nums[i] + nums[j] + nums[k])

        return -1 if minimum == math.inf else minimum


if __name__ == '__main__':
    print(Solution().minimumSum(nums=[8, 6, 1, 5, 3]))
