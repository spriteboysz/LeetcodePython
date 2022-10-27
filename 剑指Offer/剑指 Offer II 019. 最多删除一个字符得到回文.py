#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-27 23:07
FileName: 剑指Offer/剑指 Offer II 019. 最多删除一个字符得到回文.py
Description: 
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                s = s[left:right + 1]
                break
        temp1, temp2 = s[:-1], s[1:]
        return temp1 == temp1[::-1] or temp2 == temp2[::-1]


if __name__ == '__main__':
    print(Solution().validPalindrome("abca"))
