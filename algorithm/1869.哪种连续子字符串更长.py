#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-23 16:27:24
LastEditTime: 2022-01-23 16:37:33
Description: 
FilePath: 1869.哪种连续子字符串更长.py
'''
#
# @lc app=leetcode.cn id=1869 lang=python3
#
# [1869] 哪种连续子字符串更长
#

# @lc code=start
from re import S


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count = [1] * len(s)
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count[i] = count[i - 1] + 1
        maximum = set()
        for i, letter in enumerate(s):
            if count[i] == max(count):
                maximum.add(letter)
        return len(maximum) == 1 and list(maximum)[0] == "1"
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.checkZeroOnes("111000"))
