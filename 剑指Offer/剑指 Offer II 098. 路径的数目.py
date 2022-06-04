#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 22:17
LastEditTime: 2022-06-04 22:17
Description:
FilePath: 剑指 Offer II 098. 路径的数目.py
"""

from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        a, b = m + n - 2, m - 1
        return int(factorial(a) / (factorial(b) * factorial(a - b)))


if __name__ == '__main__':
    solution = Solution()
    ans = solution.uniquePaths(m=3, n=7)
    print(ans)
