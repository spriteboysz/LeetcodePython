#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-26 22:54
LastEditTime: 2022-05-26 22:54
Description:
FilePath: 剑指 Offer 12. 矩阵中的路径.py
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ""
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

if __name__ == '__main__':
    solution = Solution()
    ans = solution.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], [
        "A", "D", "E", "E"]], word="ABCCED")
    print(ans)
