#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-16 22:27:39
LastEditTime: 2022-02-16 22:36:03
Description: 
FilePath: 1347.制造字母异位词的最小步骤数.py
"""
#
# @lc app=leetcode.cn id=1347 lang=python3
#
# [1347] 制造字母异位词的最小步骤数
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = [0] * len(ascii_lowercase)
        for si, ti in zip(s, t):
            counts[ascii_lowercase.index(si)] += 1
            counts[ascii_lowercase.index(ti)] -= 1
        return sum(map(abs, counts)) // 2


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minSteps("leetcode", "practice")
    ans = solution.minSteps("anagram", "mangaar")
    ans = solution.minSteps("friend", "family")
    print(ans)
