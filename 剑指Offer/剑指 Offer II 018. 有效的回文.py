#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-15 17:53:58
LastEditTime: 2022-05-15 17:58:51
Description:
FilePath: 剑指 Offer II 018. 有效的回文.py
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for ch in s:
            if ch.isdigit():
                t += ch
            elif ch.isalpha():
                t += ch.lower()
        return t == t[::-1]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.isPalindrome("A man, a plan, a canal: Panama")
    print(ans)
