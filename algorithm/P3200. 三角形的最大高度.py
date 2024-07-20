#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-07-14 18:37
FileName: algorithm
Description:P3200. 三角形的最大高度.py 
"""

import math


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def process(n: int, m: int) -> int:
            odd = math.isqrt(n)
            even = int((math.sqrt(m * 4 + 1) - 1) / 2)
            return even * 2 + 1 if odd > even else odd * 2

        return max(process(red, blue), process(blue, red))


if __name__ == '__main__':
    print(Solution().maxHeightOfTriangle(red=2, blue=4))
