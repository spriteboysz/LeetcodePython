#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-06-01 22:27
FileName: algorithm
Description:P3158. 求出出现两次数字的 XOR 值.py 
"""
from collections import defaultdict
from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        xor = 0
        for k, v in count.items():
            if v == 2:
                xor ^= k
        return xor


if __name__ == '__main__':
    print(Solution().duplicateNumbersXOR(nums=[1, 2, 2, 1]))
