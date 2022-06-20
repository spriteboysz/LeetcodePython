#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-20 23:16
LastEditTime: 2022-06-20 23:16
Description:
FilePath: 剑指 Offer II 065. 最短的单词编码.py
"""

from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        hashset = set()
        for word in words:
            hashset.add(word)
        for i, word in enumerate(words):
            for j in range(1, len(word)):
                if word[j:] in hashset:
                    hashset.remove(word[j:])
        return sum(map(lambda el: len(el) + 1, hashset))


if __name__ == '__main__':
    solution = Solution()
    ans = solution.minimumLengthEncoding(words=["time", "me", "bell"])
    print(ans)
