#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-02 16:38
FileName: algorithm
Description:P1238. 循环码排列.py 
"""
from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        gray = [i ^ (i >> 1) for i in range(1 << n)]
        index = gray.index(start)
        return gray[index:] + gray[:index]


if __name__ == '__main__':
    print(Solution().circularPermutation(n=2, start=3))
