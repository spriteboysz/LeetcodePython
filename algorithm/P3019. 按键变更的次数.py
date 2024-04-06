#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 14:02
FileName: algorithm
Description:P3019. 按键变更的次数.py 
"""


class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        return sum([s[i] != s[i - 1] for i in range(1, len(s))])


if __name__ == '__main__':
    print(Solution().countKeyChanges("aAbBcC"))
