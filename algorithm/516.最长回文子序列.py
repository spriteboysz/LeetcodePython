#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-16 23:22
LastEditTime: 2022-06-16 23:22
Description:
FilePath: 516.最长回文子序列.py
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 2, -1, -1):  # i从n-2开始，因为i=n-1时，最长序列是1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.longestPalindromeSubseq("bbbab")
    print(ans)
