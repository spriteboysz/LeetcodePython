#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-01 23:57:49
LastEditTime: 2022-02-02 00:24:02
Description:
FilePath: 1275.找出井字棋的获胜者.py
"""
#
# @lc app=leetcode.cn id=1275 lang=python3
#
# [1275] 找出井字棋的获胜者
#

# @lc code=start
from typing import List


class Solution:
    def check(self, chess):
        if chess[0] == chess[1] == chess[2]:
            return True
        if chess[3] == chess[4] == chess[5]:
            return True
        if chess[6] == chess[7] == chess[8]:
            return True
        if chess[0] == chess[3] == chess[6]:
            return True
        if chess[1] == chess[4] == chess[7]:
            return True
        if chess[2] == chess[5] == chess[8]:
            return True
        if chess[0] == chess[4] == chess[8]:
            return True
        if chess[2] == chess[4] == chess[6]:
            return True
        else:
            return False

    def tictactoe(self, moves: List[List[int]]) -> str:
        chess = [i for i in range(9)]
        for i in range(0, len(moves), 2):
            chess[moves[i][0] * 3 + moves[i][1]] = "A"
            if self.check(chess):
                return "A"
            if i + 1 < len(moves):
                chess[moves[i + 1][0] * 3 + moves[i + 1][1]] = "B"
                if self.check(chess):
                    return "B"
            if i == 8:
                return "Draw"
        return "Pending"


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))
    print(s.tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))
    print(s.tictactoe([[0, 0], [1, 1], [2, 0], [1, 0],
          [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]))
    print(s.tictactoe([[0, 0], [1, 1]]))
