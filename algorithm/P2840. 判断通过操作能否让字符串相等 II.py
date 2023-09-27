#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-09-26 00:02
FileName: algorithm
Description:P2840. 判断通过操作能否让字符串相等 II.py 
"""
from collections import Counter


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])


if __name__ == '__main__':
    print(Solution().checkStrings(s1="abcdba", s2="cabdab"))
