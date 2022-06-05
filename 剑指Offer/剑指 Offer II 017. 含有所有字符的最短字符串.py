#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 22:42
LastEditTime: 2022-06-05 22:42
Description:
FilePath: 剑指 Offer II 017. 含有所有字符的最短字符串.py
"""

from collections import Counter
from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        pass


if __name__ == '__main__':
    solution = Solution()
    ans = solution.minWindow(s="ADOBECODEBANC", t="ABC")
    print(ans)
