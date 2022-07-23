#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-17 23:12
LastEditTime: 2022-06-17 23:12
Description:
FilePath: 1391.检查网格中是否存在有效路径.py
"""

from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        direction = {1: {(0, 1), (0, -1)}, 2: {(1, 0), (-1, 0)}, 3: {(0, -1), (1, 0)},
                     4: {(0, 1), (1, 0)}, 5: {(0, -1), (-1, 0)}, 6: {(0, 1), (-1, 0)}}
        # 每个数字对应的方向先列出
        n, m = len(grid), len(grid[0])
        flag = [[0] * m for i in range(n)]

        def dfs(x, y):
            flag[x][y] = 1
            if x == n - 1 and y == m - 1:
                return True
            for dx, dy in direction[grid[x][y]]:
                if 0 <= x + dx < n and 0 <= y + dy < m and \
                        flag[x + dx][dy + y] == 0 and (-dx, -dy) in direction[grid[x + dx][y + dy]]:
                    if dfs(x + dx, y + dy):
                        return True
            return False

        return dfs(0, 0)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.hasValidPath(grid=[[2, 4, 3], [6, 5, 2]])
    print(ans)
