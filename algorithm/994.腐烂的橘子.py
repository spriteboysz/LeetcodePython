#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-30 22:52
LastEditTime: 2022-05-30 22:52
Description:
FilePath: 994.腐烂的橘子.py
"""

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m, time, queue = len(grid), len(grid[0]), 0, []
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, time))

        while queue:
            i, j, time = queue.pop(0)
            for di, dj in directions:
                if 0 <= i + di < n and 0 <= j + dj < m and grid[i + di][j + dj] == 1:
                    grid[i + di][j + dj] = 2
                    queue.append((i + di, j + dj, time + 1))

        for row in grid:
            if 1 in row:
                return -1
        return time


if __name__ == '__main__':
    solution = Solution()
    ans = solution.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    print(ans)
