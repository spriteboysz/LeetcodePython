#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-27 17:30
FileName: algorithm
Description:P2317. 操作后的最大异或和.py 
"""
from typing import List
from functools import reduce


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x | y, nums)


if __name__ == '__main__':
    print(Solution().maximumXOR(nums=[1, 2, 3, 9, 2]))
