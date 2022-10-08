#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-16 23:27:16
LastEditTime: 2022-01-16 23:30:02
Description: 
FilePath: 796.旋转字符串.py
'''
#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False

# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.rotateString("abcde", "abced"))
    