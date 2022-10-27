#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-01 21:52:17
LastEditTime: 2022-05-01 21:54:58
Description: 
FilePath: 剑指 Offer 62. 圆圈中最后剩下的数字.py
"""


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x


if __name__ == "__main__":
    solution = Solution()
    ans = solution.lastRemaining(5, 3)
    print(ans)
    ans = solution.lastRemaining(10, 17)
    print(ans)
