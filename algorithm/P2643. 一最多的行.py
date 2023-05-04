#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-03 22:40
FileName: algorithm/P2643. 一最多的行.py
Description: 
"""
from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        rows = list(map(sum, mat))
        maximum = max(rows)
        for i, item in enumerate(rows):
            if item == maximum:
                return [i, maximum]
        return [0, 0]


if __name__ == '__main__':
    print(Solution().rowAndMaximumOnes(mat=[[0, 0, 0], [0, 1, 1]]))
