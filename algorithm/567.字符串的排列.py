#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-19 15:48:41
LastEditTime: 2022-03-19 16:08:04
Description: 
FilePath: 567.字符串的排列.py
"""
#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1count, s2curcount = [0] * 26, [0] * 26
        for item1, item2 in zip(s1, s2[: len(s1)]):
            s1count[ascii_lowercase.index(item1)] += 1
            s2curcount[ascii_lowercase.index(item2)] += 1

        if s1count == s2curcount:
            return True
        for i in range(len(s1), len(s2)):
            s2curcount[ascii_lowercase.index(s2[i - len(s1)])] -= 1
            s2curcount[ascii_lowercase.index(s2[i])] += 1
            if s1count == s2curcount:
                return True
        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.checkInclusion("ab", "eidbaooo")
    print(ans)
    ans = solution.checkInclusion("ab", "eidboaoo")
    print(ans)
    ans = solution.checkInclusion("ab", "cab")
    print(ans)
