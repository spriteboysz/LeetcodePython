#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-09-24 21:38
FileName: algorithm
Description:P2859. 计算 K 置位下标对应元素的和.py 
"""
from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum([num for i, num in enumerate(nums) if i.bit_count() == k])


if __name__ == '__main__':
    print(Solution().sumIndicesWithKSetBits(nums=[5, 10, 1, 5, 2], k=1))
