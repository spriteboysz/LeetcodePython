#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-03 21:56
FileName: algorithm/P2660. 保龄球游戏的获胜者.py
Description: 
"""
from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def process(player):
            score, n = 0, len(player)
            flag = [False] * n
            for i, item in enumerate(player):
                if item == 10:
                    if i + 1 < n:
                        flag[i + 1] = True
                    if i + 2 < n:
                        flag[i + 2] = True
                score += item * (1 + int(flag[i]))
            return score

        score1, score2 = process(player1), process(player2)
        if score1 == score2:
            return 0
        return 1 if score1 > score2 else 2


if __name__ == '__main__':
    print(Solution().isWinner(player1=[4, 10, 7, 10], player2=[6, 5, 2, 3]))
