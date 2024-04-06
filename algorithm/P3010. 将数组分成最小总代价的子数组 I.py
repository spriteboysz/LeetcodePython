#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 17:34
FileName: algorithm
Description:P3010. 将数组分成最小总代价的子数组 I.py 
"""
from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return sum(sorted(nums[1:])[:2]) + nums[0]


if __name__ == '__main__':
    print(Solution().minimumCost(nums=[10, 3, 1, 1]))
