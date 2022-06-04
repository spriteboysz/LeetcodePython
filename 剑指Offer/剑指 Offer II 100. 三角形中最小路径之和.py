#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 21:56
LastEditTime: 2022-06-04 21:56
Description:
FilePath: 剑指 Offer II 100. 三角形中最小路径之和.py
"""

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        return min(triangle[-1])

if __name__ == '__main__':
    solution = Solution()
    ans = solution.minimumTotal(
        triangle=[[2],
                  [3, 4],
                  [6, 5, 7],
                  [4, 1, 8, 3]])
    print(ans)
