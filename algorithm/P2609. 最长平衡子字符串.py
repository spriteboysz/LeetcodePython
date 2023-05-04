#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-03 23:08
FileName: algorithm/P2609. 最长平衡子字符串.py
Description: 
"""


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        for i in range(25, -1, -1):
            if s.find("0" * i + "1" * i) >= 0:
                return i * 2
        return 0


if __name__ == '__main__':
    print(Solution().findTheLongestBalancedSubstring("01000111"))
