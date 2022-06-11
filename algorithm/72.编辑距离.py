#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-11 22:26
LastEditTime: 2022-06-11 22:26
Description:
FilePath: 72.编辑距离.py
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        if n1 * n2 == 0:
            return n1 + n2
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            dp[i][0] = i
        for j in range(1, n2 + 1):
            dp[0][j] = j
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1]
                                   [j], dp[i - 1][j - 1]) + 1
        return dp[n1][n2]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.minDistance(word1="intention", word2="execution")
    print(ans)
    ans = solution.minDistance(word1="horse", word2="ros")
    print(ans)
