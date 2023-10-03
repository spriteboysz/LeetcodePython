#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-01 20:37
FileName: LCP
Description:LCR 005. 最大单词长度乘积.py 
"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = {}
        for word in words:
            value = 0
            for c in word:
                value |= 1 << (ord(c) - ord('a'))
            dic[word] = value
        maximum = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if dic[words[i]] & dic[words[j]] == 0:
                    maximum = max(maximum, len(words[i]) * len(words[j]))
        return maximum


if __name__ == '__main__':
    print(Solution().maxProduct(words=["abcw", "baz", "foo", "bar", "fxyz", "abcdef"]))
    print(Solution().maxProduct(words=["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
