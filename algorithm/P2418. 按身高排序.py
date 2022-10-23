#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-23 23:29
FileName: algorithm/P2418. 按身高排序.py
Description: 
"""
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _, name in sorted(zip(heights, names), reverse=True)]


if __name__ == '__main__':
    names = ["Alice", "Bob", "Bob"]
    heights = [155, 185, 150]
    solution = Solution().sortPeople(names, heights)
    print(solution)
