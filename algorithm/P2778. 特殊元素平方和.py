#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-23 23:11
FileName: algorithm
Description:P2778. 特殊元素平方和.py 
"""
from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum([nums[i] * nums[i] for i in range(0, len(nums)) if len(nums) % (i + 1) == 0])


if __name__ == '__main__':
    print(Solution().sumOfSquares(nums=[2, 7, 1, 19, 18, 3]))
