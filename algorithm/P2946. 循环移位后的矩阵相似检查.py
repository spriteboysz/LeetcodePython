#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-02 22:36
FileName: algorithm
Description:P2946. 循环移位后的矩阵相似检查.py 
"""
from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k %= len(mat[0])
        return k == 0 or all(r == r[k:] + r[:k] for r in mat)


if __name__ == '__main__':
    print(Solution().areSimilar(mat=[[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], k=2))
