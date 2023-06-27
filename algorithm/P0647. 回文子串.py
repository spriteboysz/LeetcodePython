#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-17 16:32:40
LastEditTime: 2022-04-17 16:35:16
Description: 
FilePath: 647.回文子串.py
"""


#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if i == j or j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        count += 1
                    # elif dp[i + 1][j - 1]:
                    #     dp[i][j] = True
                    #     count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.countSubstrings("abc")
    print(ans)
    ans = solution.countSubstrings("aaa")
    print(ans)
