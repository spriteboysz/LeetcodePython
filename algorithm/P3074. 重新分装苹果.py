#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 12:31
FileName: algorithm
Description:P3074. 重新分装苹果.py 
"""
from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total, acc = sum(apple), 0
        capacity.sort(reverse=True)
        for i, cap in enumerate(capacity):
            acc += cap
            if acc >= total:
                return i + 1
        return -1


if __name__ == '__main__':
    print(Solution().minimumBoxes(apple=[5, 5, 5], capacity=[2, 4, 2, 7]))
