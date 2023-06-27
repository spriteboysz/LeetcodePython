#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-11 23:45
LastEditTime: 2022-06-11 23:45
Description:
FilePath: 1314.矩阵区域和.py
"""

from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        p = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + mat[i - 1][j - 1]

        # print(p)

        def get(x, y):
            return p[max(min(x, n), 0)][max(min(y, m), 0)]

        block = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                block[i][j] = get(i + k + 1, j + k + 1) - get(i - k, j + k + 1) \
                              - get(i + k + 1, j - k) + get(i - k, j - k)
        return block


if __name__ == '__main__':
    solution = Solution()
    ans = solution.matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=2)
    print(ans)
    ans = solution.matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1)
    print(ans)
