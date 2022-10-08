#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-22 22:57:43
LastEditTime: 2022-01-22 23:03:08
Description: 
FilePath: 1957.删除字符使字符串变好.py
'''
#
# @lc app=leetcode.cn id=1957 lang=python3
#
# [1957] 删除字符使字符串变好
#

# @lc code=start


class Solution:
    def makeFancyString(self, s: str) -> str:
        count = [1] * len(s)
        s2 = s[0]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count[i] = count[i - 1] + 1
            if count[i] <= 2:
                s2 += s[i]
        return s2

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.makeFancyString("aab"))
