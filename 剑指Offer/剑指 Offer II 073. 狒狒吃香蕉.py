#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-20 23:34
LastEditTime: 2022-06-20 23:34
Description:
FilePath: 剑指 Offer II 073. 狒狒吃香蕉.py
"""

from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            return sum([ceil(num / k) for num in piles]) <= h

        left, right = max(1, sum(piles) // h), max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    solution = Solution()
    # ans = solution.minEatingSpeed(piles=[3, 6, 7, 11], h=8)
    # print(ans)
    # ans = solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6)
    # print(ans)
    # ans = solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5)
    # print(ans)
    ans = solution.minEatingSpeed([312884470], 968709470)
    print(ans)
