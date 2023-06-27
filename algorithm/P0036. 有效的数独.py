#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-18 23:04:04
LastEditTime: 2022-02-18 23:16:40
Description: 
FilePath: 36.有效的数独.py
"""
#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(nums):
            s = "".join(nums).replace(".", "")
            return len(s) == len(set(s))

        for row in board:
            if not check(row):
                return False
        for col in zip(*board):
            if not check(list(col)):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = (
                        board[i][j: j + 3]
                        + board[i + 1][j: j + 3]
                        + board[i + 2][j: j + 3]
                )
                if not check(block):
                    return False
        return True


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
    print(ans)
