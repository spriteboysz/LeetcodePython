#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-20 23:30:27
LastEditTime: 2022-02-20 23:54:07
Description: 
FilePath: 1138.字母板上的路径.py
"""
#
# @lc app=leetcode.cn id=1138 lang=python3
#
# [1138] 字母板上的路径
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = dict()
        k = 0
        for i in range(5):
            for j in range(5):
                board[ascii_lowercase[k]] = (i, j)
                k += 1
        board["z"] = (5, 0)

        target = "a" + target
        path = ""
        for i in range(len(target) - 1):
            x, y = (
                board[target[i + 1]][0] - board[target[i]][0],
                board[target[i + 1]][1] - board[target[i]][1],
            )
            lr = "L" if y < 0 else "R"
            du = "U" if x < 0 else "D"
            if target[i] == "z":
                path += du * abs(x) + lr * abs(y) + "!"
            else:
                path += lr * abs(y) + du * abs(x) + "!"
        return path


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.alphabetBoardPath("leet")
    print(ans)
    ans1 = solution.alphabetBoardPath("zdz")
    print(ans1)
