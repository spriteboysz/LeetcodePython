#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/28 23:15
FileName: algorithm/P2485. 找出中枢整数.py
Description: 
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(n + 1):
            if i * i * 2 == n * (n + 1):
                return i
        else:
            return -1


if __name__ == '__main__':
    print(Solution().pivotInteger(8))
    print(Solution().pivotInteger(1))
    print(Solution().pivotInteger(4))
