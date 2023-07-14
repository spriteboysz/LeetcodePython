#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-13 22:53
FileName: algorithm/P2579. 统计染色格子数.py
Description: 
"""


class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * (n - 1) + 1


if __name__ == '__main__':
    print(Solution().coloredCells(3))
