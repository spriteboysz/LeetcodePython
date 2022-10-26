#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-26 21:59
FileName: algorithm/P2399. 检查相同字母间的距离.py
Description: 
"""
from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        alphabet = [-1] * 26
        for i, c in enumerate(s):
            index = ord(c) - 97
            if alphabet[index] == -1:
                alphabet[index] = i
            else:
                alphabet[index] = i - alphabet[index] - 1
        for i in range(26):
            if alphabet[i] != -1 and alphabet[i] != distance[i]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().checkDistances(s="aa",
                                    distance=[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                              0]))
