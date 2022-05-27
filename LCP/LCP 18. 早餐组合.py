#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-27 23:29
LastEditTime: 2022-05-27 23:29
Description:
FilePath: LCP 18. 早餐组合.py
"""

from typing import List
from bisect import bisect_right

class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        count = 0
        for price in staple:
            index = bisect_right(drinks, x - price)
            count += index
        return count % (10 ** 9 + 7)

if __name__ == '__main__':
    solution = Solution()
    ans = solution.breakfastNumber(staple=[10, 20, 5], drinks=[5, 5, 2], x=15)
    print(ans)

    ans = solution.breakfastNumber(staple=[2, 1, 1], drinks=[8, 9, 5, 1], x=9)
    print(ans)
