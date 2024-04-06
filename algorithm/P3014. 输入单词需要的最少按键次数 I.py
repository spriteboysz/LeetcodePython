#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 13:38
FileName: algorithm
Description:P3014. 输入单词需要的最少按键次数 I.py 
"""


class Solution:
    def minimumPushes(self, word: str) -> int:
        div, mod = divmod(len(word), 8)
        return ((div << 2) + mod) * (div + 1)


if __name__ == '__main__':
    print(Solution().minimumPushes(word="abcde"))
