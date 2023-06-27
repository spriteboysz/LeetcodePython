#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-01 23:52:20
LastEditTime: 2022-03-02 00:07:28
Description: 
FilePath: 1763.最长的美好子字符串.py
"""
#
# @lc app=leetcode.cn id=1763 lang=python3
#
# [1763] 最长的美好子字符串
#

# @lc code=start
from string import ascii_lowercase, ascii_uppercase


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        lst = []
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                cur = s[i: j + 1]
                lower, upper = [False] * 26, [False] * 26
                for letter in cur:
                    if letter.islower():
                        lower[ascii_lowercase.index(letter)] = True
                    else:
                        upper[ascii_uppercase.index(letter)] = True
                if not any([a ^ b for a, b in zip(lower, upper)]):
                    lst.append(cur)
        return "" if not lst else sorted(lst, key=len, reverse=True)[0]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.longestNiceSubstring("YazaAay")
    print(ans)
    ans = solution.longestNiceSubstring("dDzeE")
    print(ans)
    ans = solution.longestNiceSubstring("Bb")
    print(ans)
    ans = solution.longestNiceSubstring("c")
    print(ans)
