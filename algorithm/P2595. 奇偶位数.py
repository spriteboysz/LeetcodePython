#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-04 22:44
FileName: algorithm/P2595. 奇偶位数.py
Description: 
"""
from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        bit = [0, 0]
        i = 0
        while n:
            bit[i] += n & 1
            n >>= 1
            i ^= 1
        return bit


if __name__ == '__main__':
    print(Solution().evenOddBit(17))
