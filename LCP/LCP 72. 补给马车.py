#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-10 23:30
FileName: LCP/LCP 72. 补给马车.py
Description: 
"""
from typing import List


class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        n = len(supplies)
        while len(supplies) > n // 2:
            minimum, index = supplies[0] + supplies[1], 0
            for i in range(1, len(supplies) - 1):
                cur = supplies[i] + supplies[i + 1]
                if cur < minimum:
                    minimum, index = cur, i
            supplies[index] += supplies[index + 1]
            supplies = supplies[:index + 1] + supplies[index + 2:]
        return supplies


if __name__ == '__main__':
    print(Solution().supplyWagon(supplies=[7, 3, 6, 1, 8]))
