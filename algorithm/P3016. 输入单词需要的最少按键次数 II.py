#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-01 20:47
FileName: algorithm
Description:P3016. 输入单词需要的最少按键次数 II.py 
"""


class Solution:
    def minimumPushes(self, word: str) -> int:
        alphabet = [0] * 26
        for c in word:
            alphabet[ord(c) - ord('a')] += 1
        alphabet.sort(reverse=True)
        return sum(alphabet) + sum(alphabet[8:]) + sum(alphabet[16:]) + sum(alphabet[24:])


if __name__ == '__main__':
    print(Solution().minimumPushes(word="aabbccddeeffgghhiiiiii"))
