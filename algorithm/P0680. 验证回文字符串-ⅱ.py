#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-23 22:09:33
LastEditTime: 2022-02-23 22:18:07
Description: 
FilePath: 680.验证回文字符串-ⅱ.py
"""


#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for i in range(len(s) // 2):
            j = len(s) - 1 - i
            if s[i] != s[j]:
                cur1 = s[:i] + s[i + 1:]
                cur2 = s[:j] + s[j + 1:]
                if cur1 == cur1[::-1] or cur2 == cur2[::-1]:
                    return True
                else:
                    return False


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.validPalindrome("abac")
    print(ans)
