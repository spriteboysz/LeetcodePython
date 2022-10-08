#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-24 23:17:49
LastEditTime: 2022-01-24 23:22:16
Description: 
FilePath: 1624.两个相同字符之间的最长子字符串.py
'''
#
# @lc app=leetcode.cn id=1624 lang=python3
#
# [1624] 两个相同字符之间的最长子字符串
#

# @lc code=start


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        letters = list(set(s))
        maximum = -1
        for letter in letters:
            current = s.rindex(letter) - s.index(letter) - 1
            if current > maximum:
                maximum = current
        return maximum
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maxLengthBetweenEqualCharacters("aa"))
    print(s.maxLengthBetweenEqualCharacters("abca"))
    print(s.maxLengthBetweenEqualCharacters("cbzxy"))
    print(s.maxLengthBetweenEqualCharacters("cabbac"))
