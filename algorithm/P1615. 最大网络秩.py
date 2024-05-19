#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-19 16:25
FileName: algorithm
Description:P1615. 最大网络秩.py 
"""
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        counts, seen = [0] * n, set()
        for x, y in roads:
            counts[x] += 1
            counts[y] += 1
            seen.add((min(x, y), max(x, y)))
        return max(
            num1 + num2 - int((j, i) in seen) for i, num1 in enumerate(counts) for j, num2 in enumerate(counts[:i]))


if __name__ == '__main__':
    print(Solution().maximalNetworkRank(n=5, roads=[[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]))
    print(Solution().maximalNetworkRank(n=4, roads=[[0, 1], [0, 3], [1, 2], [1, 3]]))
