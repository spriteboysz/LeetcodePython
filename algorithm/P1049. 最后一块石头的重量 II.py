#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-10 23:41
FileName: algorithm/P1049. 最后一块石头的重量 II.py
Description: 
"""
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) / 2.0
        candidates = {0}
        for stone in stones:
            addition = set()
            for candidate in candidates:
                if stone + candidate <= target:
                    addition.add(stone + candidate)
            candidates = candidates.union(addition)
        return int(2 * (target - max(candidates)))


if __name__ == '__main__':
    print(Solution().lastStoneWeightII(stones=[2, 7, 4, 1, 8, 1]))
