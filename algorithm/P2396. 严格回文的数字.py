#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-22 20:00
FileName: algorithm/P2396. 严格回文的数字.py
Description: 
"""


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        if n < 0:
            return False
        return False


if __name__ == '__main__':
    solution = Solution().isStrictlyPalindromic(10)
    print(solution)
