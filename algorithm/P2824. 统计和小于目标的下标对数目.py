#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-22 23:29
FileName: algorithm
Description:P2824. 统计和小于目标的下标对数目.py 
"""
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        return sum([1 for i in range(0, n) for j in range(i + 1, n) if nums[i] + nums[j] < target])


if __name__ == '__main__':
    print(Solution().countPairs(nums=[-6, 2, 5, -2, -7, -1, 3], target=-2))
