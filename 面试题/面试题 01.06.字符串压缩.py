#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 23:15:41
LastEditTime: 2022-02-04 23:23:02
Description: 
FilePath: 100161.字符串压缩.py
'''
#
# @lc app=leetcode.cn id=100161 lang=python3
#
# [面试题 01.06] 字符串压缩
#

# @lc code=start


class Solution:
    def compressString(self, s: str) -> str:
        count = [1] * len(s)
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                count[i] = count[i - 1] + 1
                count[i - 1] = 0
        s2 = ""
        for l, c in zip(s, count):
            if c != 0:
                s2 += l + str(c)
        return s2 if len(s2) < len(s) else s

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.compressString("aabcccccaaa"))
    print(s.compressString("abbccd"))
