#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-07-14 10:32
FileName: algorithm
Description:P3210. 找出加密后的字符串.py 
"""


class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k %= len(s)
        return s[k:] + s[:k]


if __name__ == '__main__':
    print(Solution().getEncryptedString(s="dart", k=3))
    print(Solution().getEncryptedString(s="fvevzh", k=10))
