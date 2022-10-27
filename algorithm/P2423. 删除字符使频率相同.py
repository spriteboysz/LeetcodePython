#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-27 22:51
FileName: algorithm/P2423. 删除字符使频率相同.py
Description: 
"""
from collections import defaultdict


class Solution:
    def equalFrequency(self, word: str) -> bool:
        alphabet = defaultdict(int)
        for c in word:
            alphabet[c] += 1
        alphabet = sorted(alphabet.values())

        return len(alphabet) == 1 or (alphabet[0] == 1 and alphabet[1] == alphabet[-1]) or alphabet[0] == alphabet[-2] == alphabet[-1] - 1


if __name__ == '__main__':
    print(Solution().equalFrequency("abcc"))
    print(Solution().equalFrequency("aazz"))
    print(Solution().equalFrequency("a"))
