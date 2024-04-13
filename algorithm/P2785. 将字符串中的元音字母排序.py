#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-13 18:10
FileName: algorithm
Description:P2785. 将字符串中的元音字母排序.py 
"""


class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_alphabet = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels = [c for c in s if c in vowel_alphabet]
        vowels.sort()
        ss = []
        for c in s:
            if c in vowel_alphabet:
                ss.append(vowels[0])
                vowels.pop(0)
            else:
                ss.append(c)
        return ''.join(ss)


if __name__ == '__main__':
    print(Solution().sortVowels(s="lEetcOde"))
