#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-24 22:34
FileName: algorithm/P2710. 移除字符串中的尾随零.py
Description: 
"""


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for i, c in enumerate(reversed(num)):
            if c != '0':
                return num if i == 0 else num[:-i]


if __name__ == '__main__':
    print(Solution().removeTrailingZeros("51230100"))
    print(Solution().removeTrailingZeros("123"))
