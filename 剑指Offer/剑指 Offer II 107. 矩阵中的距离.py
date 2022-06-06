#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-06 23:31
LastEditTime: 2022-06-06 23:31
Description:
FilePath: 剑指 Offer II 107. 矩阵中的距离.py
"""

from typing import List
from collections import deque
from math import inf


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        distance, queue = [[0 for _ in range(m)] for _ in range(n)], deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    distance[i][j] = inf

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                row, col = x + dx, y + dy
                if 0 <= row < n and 0 <= col < m and distance[row][col] > distance[x][y] + 1:
                    distance[row][col] = distance[x][y] + 1
                    queue.append((row, col))
        return distance


if __name__ == '__main__':
    solution = Solution()
    ans = solution.updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    print(ans)
    ans = solution.updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]])
    print(ans)
