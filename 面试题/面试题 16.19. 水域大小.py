#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-07 22:51
LastEditTime: 2022-06-07 22:51
Description:
FilePath: 面试题 16.19. 水域大小.py
"""

from typing import List

class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:

        def dfs(i, j):
            count, land[i][j] = 1, 1
            for x, y in [(i + dx, j + dy) for dx in range(-1, 2)
                         for dy in range(-1, 2)]:
                if 0 <= x < n and 0 <= y < m and land[x][y] == 0:
                    count += dfs(x, y)
            return count

        n, m, sizes = len(land), len(land[0]), []
        return sorted([dfs(i, j) for i in range(n)
                       for j in range(m) if not land[i][j]])

if __name__ == '__main__':
    solution = Solution()
    ans = solution.pondSizes([
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ])
    print(ans)
