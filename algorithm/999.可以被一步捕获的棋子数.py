#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-25 23:09:10
LastEditTime: 2022-04-25 23:09:58
Description: 
FilePath: 999.可以被一步捕获的棋子数.py
"""
#
# @lc app=leetcode.cn id=999 lang=python3
#
# [999] 可以被一步捕获的棋子数
#

# @lc code=start
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    r, c = i, j
                    break

        rows = "".join(board[r]).replace(".", "")
        cols = "".join(list(zip(*board))[c]).replace(".", "")
        target = rows + "#" + cols
        return target.count("pR") + target.count("Rp")


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.numRookCaptures(
        [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", "R", ".", ".", ".", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )
    print(ans)

    ans = solution.numRookCaptures(
        [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", "p", "p", "p", "p", "p", ".", "."],
            [".", "p", "p", "B", "p", "p", ".", "."],
            [".", "p", "B", "R", "B", "p", ".", "."],
            [".", "p", "p", "B", "p", "p", ".", "."],
            [".", "p", "p", "p", "p", "p", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )
    print(ans)
