#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-13 00:09:32
LastEditTime: 2022-04-13 00:15:51
Description: 
FilePath: 2225.找出输掉零场或一场比赛的玩家.py
"""
#
# @lc app=leetcode.cn id=2225 lang=python3
#
# [2225] 找出输掉零场或一场比赛的玩家
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = [], []
        for win, lose in matches:
            winners.append(win)
            losers.append(lose)
        return [
            sorted(set(winners) - set(losers)),
            sorted([k for k, v in Counter(losers).items() if v == 1]),
        ]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findWinners(
        matches=[
            [1, 3],
            [2, 3],
            [3, 6],
            [5, 6],
            [5, 7],
            [4, 5],
            [4, 8],
            [4, 9],
            [10, 4],
            [10, 9],
        ]
    )
    print(ans)

    ans = solution.findWinners(matches=[[2, 3], [1, 3], [5, 4], [6, 4]])
    print(ans)
