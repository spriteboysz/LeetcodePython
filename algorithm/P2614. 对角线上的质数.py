#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-03 22:57
FileName: algorithm/P2614. 对角线上的质数.py
Description: 
"""
import math
from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(num):
            if num == 1:
                return False
            for el in range(2, int(math.sqrt(num)) + 1):
                if num % el == 0:
                    return False
            return True

        diagonal = []
        for i, row in enumerate(nums):
            if isPrime(row[i]):
                diagonal.append(row[i])
            if isPrime(row[-1 - i]):
                diagonal.append(row[-1 - i])
        return 0 if len(diagonal) == 0 else max(diagonal)


if __name__ == '__main__':
    print(Solution().diagonalPrime(nums=[[1, 2, 3], [5, 6, 7], [9, 10, 11]]))
