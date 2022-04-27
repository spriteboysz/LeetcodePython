#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-27 22:23:13
LastEditTime: 2022-04-27 22:23:33
Description: 
FilePath: 583.两个字符串的删除操作.py
"""
#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 边界状态
        for j in range(1, n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            dp[i][0] = i

        # 状态更新
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[m][n]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minDistance("sea", "eat")
    print(ans)
    ans = solution.minDistance(word1="leetcode", word2="etco")
    print(ans)
