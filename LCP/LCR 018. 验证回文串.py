#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-01 22:47
FileName: LCP
Description:LCR 018. 验证回文串.py 
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for c in s:
            if c.isalnum():
                ss += c.lower()
        return ss == ss[::-1]


if __name__ == '__main__':
    print(Solution().isPalindrome(s="A man, a plan, a canal: Panama"))
