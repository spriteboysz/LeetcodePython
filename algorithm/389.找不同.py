#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-27 23:10:07
Description: 
FilePath: 389.找不同.py
'''
#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for item in s:
            t = t.replace(item, "", 1)

        return str(t)
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.findTheDifference("abcd", "abcde")
