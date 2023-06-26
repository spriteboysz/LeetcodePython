#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-11 22:47:43
LastEditTime: 2022-01-11 23:02:19
Description:
FilePath: 345.反转字符串中的元音字母.py
"""
#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        vowels = ""
        for item in s:
            if item in vowel:
                vowels += item
        vowels = vowels[::-1]
        s2, i = "", 0
        for item in s:
            if item in vowel:
                s2 += vowels[i]
                i += 1
            else:
                s2 += item
        return s2
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.reverseVowels("leetcode"))
