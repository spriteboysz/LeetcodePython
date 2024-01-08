#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-08 22:52
FileName: algorithm
Description:P2894. 分类求和并作差.py 
"""


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        diff = 0
        for i in range(1, n + 1):
            if i % m == 0:
                diff -= i
            else:
                diff += i
        return diff


if __name__ == '__main__':
    print(Solution().differenceOfSums(n=10, m=3))
