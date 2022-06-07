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

        def dfs(x, y):
            count, land[x][y] = 1, 1
            for i, j in [(x + dx, y + dy) for dx in [-1, 0, 1]
                         for dy in [-1, 0, 1]]:
                if 0 <= i < n and 0 <= j < m and land[i][j] == 0:
                    count += dfs(i, j)
            return count

        n, m = len(land), len(land[0])
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
