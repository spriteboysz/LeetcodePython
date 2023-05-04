#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-04 22:54
FileName: algorithm/P2582. 递枕头.py
Description: 
"""


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pos, direction = 1, 1
        for _ in range(0, time):
            pos += direction
            if pos == n or pos == 1:
                direction *= -1
        return pos


if __name__ == '__main__':
    print(Solution().passThePillow(4, 5))
