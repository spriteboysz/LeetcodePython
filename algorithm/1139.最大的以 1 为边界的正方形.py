#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-09 23:09
LastEditTime: 2022-06-09 23:09
Description:
FilePath: 1139.最大的以 1 为边界的正方形.py
"""

from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        pass


if __name__ == '__main__':
    solution = Solution()
    ans = solution.largest1BorderedSquare(
        grid=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    print(ans)
