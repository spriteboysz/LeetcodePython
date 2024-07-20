#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-07-20 20:38
FileName: algorithm
Description:P3216. 交换后字典序最小的字符串.py 
"""


class Solution:
    def getSmallestString(self, s: str) -> str:
        ss = list(map(int, s))
        for i in range(1, len(ss)):
            a, b = ss[i - 1], ss[i]
            if not ((a % 2) ^ (b % 2)) and a > b:
                ss[i - 1], ss[i] = ss[i], ss[i - 1]
                break
        return ''.join(map(str, ss))


if __name__ == '__main__':
    print(Solution().getSmallestString("45320"))
