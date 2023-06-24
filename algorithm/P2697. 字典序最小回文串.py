#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-24 22:45
FileName: algorithm/P2697. 字典序最小回文串.py
Description: 
"""


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ss = list(s)
        for i in range(0, len(s) // 2):
            c = min(ss[i], ss[- 1 - i])
            ss[i] = c
            ss[- 1 - i] = c
        return "".join(ss)


if __name__ == '__main__':
    print(Solution().makeSmallestPalindrome(s="egcfe"))
