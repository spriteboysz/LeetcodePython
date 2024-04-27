#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-27 17:56
FileName: algorithm
Description:P2997. 使数组异或和等于 K 的最少操作次数.py 
"""
from functools import reduce
from operator import xor
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return (reduce(xor, nums) ^ k).bit_count()


if __name__ == '__main__':
    print(Solution().minOperations(nums=[2, 1, 3, 4], k=1))
