#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-22 20:13
FileName: algorithm/P2413. 最小偶倍数.py
Description: 
"""


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2


if __name__ == '__main__':
    solution = Solution().smallestEvenMultiple(10)
    print(solution)
