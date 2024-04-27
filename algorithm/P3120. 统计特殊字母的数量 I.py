#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-27 13:06
FileName: algorithm
Description:P3120. 统计特殊字母的数量 I.py 
"""


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        alphabet = [0] * 26
        for c in word:
            if c.islower():
                alphabet[ord(c) - ord('a')] |= 1
            else:
                alphabet[ord(c) - ord('A')] |= 2
        return alphabet.count(3)


if __name__ == '__main__':
    print(Solution().numberOfSpecialChars(word="aaAbcBC"))
