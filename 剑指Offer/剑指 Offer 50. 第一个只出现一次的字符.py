#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-04 22:03:44
LastEditTime: 2022-02-04 22:18:05
Description:
FilePath: 100316.第一个只出现一次的字符.py
"""
#
# @lc app=leetcode.cn id=100316 lang=python3
#
# [剑指 Offer 50] 第一个只出现一次的字符
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def firstUniqChar(self, s: str) -> str:
        index = []
        for letter in ascii_lowercase:
            if s.count(letter) == 1:
                index.append(s.index(letter))
        return " " if len(index) == 0 else s[min(index)]


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar(""))
    print(s.firstUniqChar("abaccdeff"))
