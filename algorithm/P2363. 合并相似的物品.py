#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-23 23:40
FileName: algorithm/P2363. 合并相似的物品.py
Description: 
"""
from collections import defaultdict
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items = defaultdict(int)
        for item in items1:
            items[item[0]] = item[1]
        for item in items2:
            items[item[0]] += item[1]
        return [[k, v] for k, v in sorted(items.items())]


if __name__ == '__main__':
    items1 = [[1, 1], [3, 2], [2, 3]]
    items2 = [[2, 1], [3, 2], [1, 3]]
    solution = Solution().mergeSimilarItems(items1, items2)
    print(solution)
