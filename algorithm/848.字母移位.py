#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-27 10:28:42
LastEditTime: 2022-02-27 10:38:42
Description: 
FilePath: 848.字母移位.py
"""
#
# @lc app=leetcode.cn id=848 lang=python3
#
# [848] 字母移位
#

# @lc code=start
from typing import List
from string import ascii_lowercase


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifted = ""
        for i in range(len(s) - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        for i in range(len(s)):
            shifted += ascii_lowercase[(ascii_lowercase.index(s[i]) + shifts[i]) % 26]
        return shifted


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.shiftingLetters("abc", [3, 5, 9])
    print(ans)
