#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-15 21:37
FileName: algorithm
Description:P3146. 两个字符串的排列差.py 
"""


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        alphabet1, alphabet2 = [0] * 26, [0] * 26
        for i, c in enumerate(s):
            alphabet1[ord(c) - ord('a')] = i
        for i, c in enumerate(t):
            alphabet2[ord(c) - ord('a')] = i
        return sum(abs(alphabet1[i] - alphabet2[i]) for i in range(26))


if __name__ == '__main__':
    print(Solution().findPermutationDifference(s="abc", t="bac"))
