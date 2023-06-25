#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-24 23:21
FileName: LCP/LCP 77. 符文储备.py
Description: 
"""
from itertools import pairwise
from typing import List


class Solution:
    def runeReserve(self, runes: List[int]) -> int:
        runes.sort()
        maximum, cnt = 1, 1
        for pre, cur in pairwise(runes):
            if cur - pre > 1:
                cnt = 1
            else:
                cnt += 1
                maximum = max(maximum, cnt)
        return maximum


if __name__ == '__main__':
    print(Solution().runeReserve(runes=[1, 3, 5, 4, 1, 7]))
