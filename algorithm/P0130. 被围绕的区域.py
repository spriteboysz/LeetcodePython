#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-25 23:50:01
LastEditTime: 2022-04-25 23:58:52
Description:
FilePath: 130.被围绕的区域.py
"""
#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(x, y):
            if 0 <= x < n and 0 <= y < m and board[x][y] == "O":
                board[x][y] = "Y"
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)

        n, m = len(board), len(board[0])
        for i in [0, n - 1]:
            for j in range(m):
                dfs(i, j)
        for i in range(n):
            for j in [0, m - 1]:
                dfs(i, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Y":
                    board[i][j] = "O"

        # for row in board:
        #     print(row)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    solution.solve(
        board=[
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
    )
