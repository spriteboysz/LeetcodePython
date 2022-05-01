#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-01 22:23:23
LastEditTime: 2022-05-01 22:39:08
Description: 
FilePath: 剑指 Offer II 034. 外星语言是否排序.py
"""

from typing import List
from string import ascii_lowercase as lower


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i, word in enumerate(words):
            cur = ""
            for letter in word:
                cur += lower[order.index(letter)]
            words[i] = cur
        return sorted(words) == words


if __name__ == "__main__":
    solution = Solution()
    ans = solution.isAlienSorted(
        words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"
    )
    print(ans)
    ans = solution.isAlienSorted(
        words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"
    )
    print(ans)
    ans = solution.isAlienSorted(
        words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"
    )
    print(ans)
