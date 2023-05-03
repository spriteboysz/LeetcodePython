#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-03 22:14
FileName: algorithm/P2652. 倍数求和.py
Description: 
"""


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        summation = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                summation += i
        return summation


if __name__ == '__main__':
    print(Solution().sumOfMultiples(10))
