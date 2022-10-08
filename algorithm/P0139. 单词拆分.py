#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-30 22:27:27
LastEditTime: 2022-04-30 22:31:24
Description: 
FilePath: 139.单词拆分.py
"""
#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.wordBreak(s="leetcode", wordDict=["leet", "code"])
    print(ans)
    ans = solution.wordBreak(s="applepenapple", wordDict=["apple", "pen"])
    print(ans)
    ans = solution.wordBreak(
        s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]
    )
    print(ans)
