#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-11 23:02
FileName: LCP/P2154. 将找到的值乘以 2.py
Description: 
"""
from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2
        return original


if __name__ == '__main__':
    print(Solution().findFinalValue(nums=[5, 3, 6, 1, 12], original=3))
