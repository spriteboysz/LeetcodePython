#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-26 22:47
FileName: algorithm/P2404. 出现最频繁的偶数元素.py
Description: 
"""
from collections import defaultdict
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        for num in filter(lambda el: el % 2 == 0, nums):
            hash[num] += 1
        if len(hash) == 0:
            return -1
        most = max(hash.values())
        return min([k for k, v in hash.items() if v == most])


if __name__ == '__main__':
    print(Solution().mostFrequentEven([0, 1, 2, 2, 4, 4, 1]))
    print(Solution().mostFrequentEven([1, 3, 5, 7]))
