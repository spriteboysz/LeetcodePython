#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-26 23:17:08
LastEditTime: 2022-04-26 23:23:16
Description: 
FilePath: 289.生命游戏.py
"""
#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def neighbor(i, j):
            res = []
            for k in range(i - 1, i + 2):
                for r in range(j - 1, j + 2):
                    if 0 <= k < m and 0 <= r < n and (k != i or j != r):
                        res.append([k, r])
            return res

        for i in range(m):
            for j in range(n):
                for x, y in neighbor(i, j):
                    if board[x][y] % 2 == 1:
                        board[i][j] += 2
        for i in range(m):
            for j in range(n):
                if 4 < board[i][j] < 8:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

# @lc code=end
