#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 17:17
FileName: algorithm
Description:P3042. 统计前后缀下标对 I.py 
"""
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt = 0
        for i, word1 in enumerate(words):
            for word2 in words[i + 1:]:
                if word2.startswith(word1) and word2.endswith(word1):
                    cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().countPrefixSuffixPairs(words=["a", "aba", "ababa", "aa"]))
