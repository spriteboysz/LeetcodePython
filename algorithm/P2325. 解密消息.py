#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-23 23:00
FileName: algorithm/P2325. 解密消息.py
Description: 
"""
from collections import defaultdict


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = defaultdict(int)
        index = 1
        for c in filter(lambda el: 'a' <= el <= 'z', list(key)):
            if alphabet[c] == 0:
                alphabet[c] = index
                index += 1
        decode = ""
        for c in message:
            if 'a' <= c <= 'z':
                decode += chr(97 + alphabet[c] - 1)
            else:
                decode += c
        return decode


if __name__ == '__main__':
    key = "eljuxhpwnyrdgtqkviszcfmabo"
    message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
    solution = Solution().decodeMessage(key, message)
    print(solution)
