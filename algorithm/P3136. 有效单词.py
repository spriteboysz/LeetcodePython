#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-08 21:38
FileName: algorithm
Description:P3136. 有效单词.py 
"""


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        flag1, flag2 = False, False
        for c in word:
            if not c.isalnum():
                return False
            if c.isalpha():
                if c in vowel:
                    flag1 = True
                else:
                    flag2 = True
        return flag1 and flag2


if __name__ == '__main__':
    print(Solution().isValid(word="234Adas"))
