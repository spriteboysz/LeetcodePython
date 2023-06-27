#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-09 23:29:02
LastEditTime: 2022-03-09 23:47:20
Description: 
FilePath: 438.找到字符串中所有字母异位词.py
"""
#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

from string import ascii_lowercase
# @lc code=start
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        s_count, p_count = [0] * 26, [0] * 26
        for i in range(len(p)):
            p_count[ascii_lowercase.index(p[i])] += 1
            s_count[ascii_lowercase.index(s[i])] += 1

        anagrams = []
        for i in range(len(s) - len(p) + 1):
            if p_count == s_count:
                anagrams.append(i)
            if i == len(s) - len(p):
                continue
            s_count[ascii_lowercase.index(s[i])] -= 1
            s_count[ascii_lowercase.index(s[i + len(p)])] += 1

        return anagrams


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.findAnagrams(s="cbaebabacd", p="abc")
    print(ans)
