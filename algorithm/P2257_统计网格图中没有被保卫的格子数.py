#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-29 18:00
LastEditTime: 2022-05-29 18:00
Description:
FilePath: 2257.统计网格图中没有被保卫的格子数.py
"""

from typing import List


class Solution:
    def countUnguarded(self,
                       m: int,
                       n: int,
                       guards: List[List[int]],
                       walls: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]
        for x, y in guards:
            matrix[x][y] = "G"
        for x, y in walls:
            matrix[x][y] = "W"
        visited = set()
        move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for x, y in guards:
            for i, j in move:
                dx, dy = x + i, y + j
                while 0 <= dx < m and 0 <= dy < n and matrix[dx][dy] == 0:
                    visited.add((dx, dy))
                    dx, dy = dx + i, dy + j
        return m * n - len(visited) - len(guards) - len(walls)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.countUnguarded(m=4, n=6, guards=[[0, 0], [1, 1], [
                                  2, 3]], walls=[[0, 1], [2, 2], [1, 4]])
    print(ans)
