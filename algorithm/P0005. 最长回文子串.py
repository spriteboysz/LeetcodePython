#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-22 22:47:36
LastEditTime: 2022-03-22 22:49:46
Description: 
FilePath: 5.最长回文子串.py
"""


#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        for j in range(len(s) - 1, 0, -1):
            for i in range(len(s) - j):
                cur = s[i: i + j + 1]
                if cur == cur[::-1]:
                    return cur
        return s[0]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.longestPalindrome("babad")
    print(ans)
