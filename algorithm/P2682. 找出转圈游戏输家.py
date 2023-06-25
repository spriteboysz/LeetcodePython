#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-24 22:59
FileName: algorithm/P2682. 找出转圈游戏输家.py
Description: 
"""
from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visited = [False] * n
        i, d = 0, k
        while not visited[i]:
            visited[i] = True
            i = (i + d) % n
            d += k
        return [i + 1 for i, el in enumerate(visited) if not el]


if __name__ == '__main__':
    print(Solution().circularGameLosers(n=5, k=2))
