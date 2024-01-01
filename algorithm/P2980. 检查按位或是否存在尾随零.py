#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-01 21:35
FileName: algorithm
Description:P2980. 检查按位或是否存在尾随零.py 
"""
from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return len(list(filter(lambda num: num % 2 == 0, nums))) >= 2


if __name__ == '__main__':
    print(Solution().hasTrailingZeros(nums=[1, 2, 3, 4, 5]))
