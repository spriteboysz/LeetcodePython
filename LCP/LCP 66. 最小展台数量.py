#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-23 23:51
FileName: LCP/LCP 66. 最小展台数量.py
Description: 
"""
from typing import List


class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        alphabet = [0] * 26
        for word in demand:
            cur = [0] * 26
            for c in word:
                cur[ord(c) - 97] += 1
            for i in range(26):
                alphabet[i] = max(alphabet[i], cur[i])
        return sum(alphabet)


if __name__ == '__main__':
    solution = Solution().minNumBooths(["acd", "bed", "accd"])
    print(solution)
    solution = Solution().minNumBooths(["abc", "ab", "ac", "b"])
    print(solution)
