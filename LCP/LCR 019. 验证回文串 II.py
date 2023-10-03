#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-01 22:51
FileName: LCP
Description:LCR 019. 验证回文串 II.py 
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(s):
            return s == s[::-1]

        if s == s[::-1]:
            return True
        for i in range((n := len(s)) // 2):
            if s[i] != s[n - 1 - i]:
                return check(s[:i] + s[i + 1:]) or check(s[:n - 1 - i] + s[n - i:])


if __name__ == '__main__':
    print(Solution().validPalindrome("abca"))
    print(Solution().validPalindrome("abc"))
