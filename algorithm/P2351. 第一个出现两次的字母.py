#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-23 11:01
FileName: algorithm/P2351. 第一个出现两次的字母.py
Description: 
"""
from collections import defaultdict


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = defaultdict(bool)
        for c in s:
            if dic[c]:
                return c
            else:
                dic[c] = True


if __name__ == '__main__':
    solution = Solution().repeatedCharacter("abcdd")
    print(solution)
