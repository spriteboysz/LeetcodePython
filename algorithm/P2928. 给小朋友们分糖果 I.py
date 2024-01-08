#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-04 23:27
FileName: algorithm
Description:P2928. 给小朋友们分糖果 I.py 
"""


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        cnt = 0
        for x in range(limit + 1):
            for y in range(limit + 1):
                if x + y > n:
                    break
                for z in range(limit + 1):
                    if x + y + z == n:
                        cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().distributeCandies(n=5, limit=2))
