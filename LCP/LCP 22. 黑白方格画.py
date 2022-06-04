#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 10:36
LastEditTime: 2022-06-04 10:36
Description:
FilePath: LCP 22. 黑白方格画.py
"""

from math import factorial


class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        if k == 0 or k == n * n:
            return 1

        def combination(a):
            return factorial(n) // (factorial(a) * factorial(n - a))

        count = 0
        for a in range(n + 1):
            for b in range(n + 1):
                if (a + b) * n - a * b == k:
                    count += combination(a) * combination(b)
        return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.paintingPlan(2, 2)
    print(ans)
