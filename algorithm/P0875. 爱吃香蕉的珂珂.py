#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-12 22:49
FileName: algorithm/P0875. 爱吃香蕉的珂珂.py
Description: 
"""
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            sumt = sum(math.ceil(pile / mid) for pile in piles)
            if sumt > h:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8))
