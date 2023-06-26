#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-03 22:22:33
LastEditTime: 2022-02-03 22:31:17
Description:
FilePath: 392.判断子序列.py
"""
#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahb"))
    print(s.isSubsequence("axc", "ahbgdc"))
