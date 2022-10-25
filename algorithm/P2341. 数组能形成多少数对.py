#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-25 23:45
FileName: algorithm/P2341. 数组能形成多少数对.py
Description: 
"""
from collections import defaultdict
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hash = defaultdict(int)
        for num in nums:
            hash[num] += 1
        double, single = 0, 0
        for v in hash.values():
            double += v // 2
            single += v % 2
        return [double, single]


if __name__ == '__main__':
    solution = Solution().numberOfPairs([1, 3, 2, 1, 3, 2, 2])
    print(solution)
