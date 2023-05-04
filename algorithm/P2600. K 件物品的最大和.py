#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-03 23:35
FileName: algorithm/P2600. K 件物品的最大和.py
Description: 
"""


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        return sum(([1] * numOnes + [0] * numZeros + [-1] * numNegOnes)[:k])


if __name__ == '__main__':
    print(Solution().kItemsWithMaximumSum(numOnes=3, numZeros=2, numNegOnes=0, k=2))
