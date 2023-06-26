#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-19 22:15:54
LastEditTime: 2022-01-19 22:23:46
Description:
FilePath: 917.仅仅反转字母.py
"""
#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
from string import ascii_letters


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = ""
        for item in s:
            if item in ascii_letters:
                letters += item

        s2, index = "", -1
        for item in s:
            if item in ascii_letters:
                s2 += letters[index]
                index -= 1
            else:
                s2 += item
        return s2


# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
