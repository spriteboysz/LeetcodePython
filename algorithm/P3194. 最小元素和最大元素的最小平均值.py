#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-06-25 23:16
FileName: algorithm
Description:P3194. 最小元素和最大元素的最小平均值.py 
"""
import math
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        minimum = math.inf
        n = len(nums)
        for i in range(n // 2):
            minimum = min((nums[i] + nums[n - i - 1]) / 2, minimum)
        return minimum


if __name__ == '__main__':
    print(Solution().minimumAverage(nums=[1, 9, 8, 3, 10, 5]))
