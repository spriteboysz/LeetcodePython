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
        start, lst = 0, list(range(n))
        while len(lst) > 1:
            start = (start + m - 1) % len(lst)
            lst.pop(start)
        return lst[0]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.lastRemaining(5, 3)
    print(ans)
    ans = solution.lastRemaining(10, 17)
    print(ans)
