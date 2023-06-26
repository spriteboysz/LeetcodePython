#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-01 22:20:44
LastEditTime: 2022-02-01 22:29:07
Description:
FilePath: 1974.使用特殊打字机键入单词的最少时间.py
"""
#
# @lc app=leetcode.cn id=1974 lang=python3
#
# [1974] 使用特殊打字机键入单词的最少时间
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def minTimeToType(self, word: str) -> int:
        count, cur = 0, "a"
        for letter in word:
            step = abs(ascii_lowercase.index(letter) -
                       ascii_lowercase.index(cur))
            count += min(step, 26 - step)
            cur = letter
        return count + len(word)

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.minTimeToType("bza"))
    print(s.minTimeToType("zjpc"))
