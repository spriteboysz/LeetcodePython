#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-03 23:00:17
LastEditTime: 2022-02-03 23:07:28
Description: 
FilePath: 459.重复的子字符串.py
'''
#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0 and s[:i] * (len(s) // i) == s:
                return True
        return False
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.repeatedSubstringPattern("abab"))
    print(s.repeatedSubstringPattern("aba"))
    print(s.repeatedSubstringPattern("abcabcabcabc"))
