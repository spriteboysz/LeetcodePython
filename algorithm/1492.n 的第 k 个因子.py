#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-15 23:25
LastEditTime: 2022-06-15 23:25
Description:
FilePath: 1492.n 的第 k 个因子.py
"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n + 1):
            if n % i == 0:
                k -= 1
            if k == 0:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    ans = solution.kthFactor(12, 3)
    print(ans)
    ans = solution.kthFactor(7, 2)
    print(ans)
    ans = solution.kthFactor(4, 4)
    print(ans)
