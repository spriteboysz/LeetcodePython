#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-04-17 17:16:42
LastEditTime: 2022-04-17 17:26:12
Description: 
FilePath: 174.地下城游戏.py
'''
#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#

# @lc code=start
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        hp = [[0] * m for _ in range(n)]
        hp[0][0] = dungeon[0][0]
        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    hp[i][j] = dungeon[i][j]
                elif i == 0:
                    hp[i][j] = hp[i][j - 1] + dungeon[i][j]
                elif j == 0:
                    hp[i][j] = hp[i - 1][j] + dungeon[i][j]
                else:
                    hp[i][j] = max(hp[i - 1][j], hp[i][j - 1]) + dungeon[i][j]
        for row in hp:
            print(row)
        return abs(hp[n - 1][m - 1]) + 1


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
    print(ans)
