#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-19 21:56
LastEditTime: 2022-06-19 21:56
Description:
FilePath: 剑指 Offer 60. n个骰子的点数.py
"""

from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [[0] * (6 * n + 1) for _ in range(n + 1)]
        for i in range(1, 7):
            dp[1][i] = 1
        for i in range(2, n + 1):
            for j in range(1, 6 * i + 1):
                for k in range(1, 7):
                    if j >= k + 1:
                        dp[i][j] += dp[i - 1][j - k]
        return list(map(lambda el: el / 6 ** n, dp[-1][n:]))


if __name__ == '__main__':
    solution = Solution()
    ans = solution.dicesProbability(2)
    print(ans)
