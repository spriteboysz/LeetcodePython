#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-25 22:20
FileName: algorithm/P2657. 找到两个数组的前缀公共数组.py
Description: 
"""
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        diff = []
        visited = set()
        for i, (num1, num2) in enumerate(zip(A, B)):
            visited.add(num1)
            visited.add(num2)
            diff.append((i + 1) * 2 - len(visited))
        return diff


if __name__ == '__main__':
    print(Solution().findThePrefixCommonArray(A=[1, 3, 2, 4], B=[3, 1, 2, 4]))
