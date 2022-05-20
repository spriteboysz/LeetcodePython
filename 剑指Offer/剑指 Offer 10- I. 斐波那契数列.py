#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-19 23:48:32
LastEditTime: 2022-05-19 23:50:04
Description: 
FilePath: 剑指 Offer 10- I. 斐波那契数列.py
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, (a + b) % 1000000007
        return b


if __name__ == "__main__":
    solution = Solution()
    ans = solution.fib(100)
    print(ans)
