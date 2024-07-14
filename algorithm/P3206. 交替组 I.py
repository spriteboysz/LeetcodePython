#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-07-14 10:43
FileName: algorithm
Description:P3206. 交替组 I.py 
"""
from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colors = colors + colors[:2]
        return sum(colors[i] != colors[i + 1] != colors[i + 2] for i in range(len(colors) - 2))


if __name__ == '__main__':
    print(Solution().numberOfAlternatingGroups(colors=[0, 1, 0, 0, 1]))
