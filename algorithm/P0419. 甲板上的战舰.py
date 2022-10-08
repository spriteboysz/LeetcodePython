#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-19 22:53:43
LastEditTime: 2022-02-19 22:56:34
Description: 
FilePath: 419.甲板上的战舰.py
"""
#
# @lc app=leetcode.cn id=419 lang=python3
#
# [419] 甲板上的战舰
#

# @lc code=start
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n, m = len(board), len(board[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == "X":
                    if (i == 0 or board[i - 1][j] == ".") and (
                        j == 0 or board[i][j - 1] == "."
                    ):
                        count += 1
        return count


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.countBattleships([["."]])
    print(ans)