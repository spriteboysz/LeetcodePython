#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 12:23
FileName: algorithm
Description:P3065. 超过阈值的最少操作数 I.py 
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum([1 for num in nums if num < k])


if __name__ == '__main__':
    print(Solution().minOperations(nums=[2, 11, 10, 1, 3], k=10))
