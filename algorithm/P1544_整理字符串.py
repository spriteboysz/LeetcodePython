#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-29 22:24:43
LastEditTime: 2022-01-29 22:31:21
Description: 
FilePath: 1544.整理字符串.py
'''
#
# @lc app=leetcode.cn id=1544 lang=python3
#
# [1544] 整理字符串
#

# @lc code=start


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for item in s:
            if len(stack) and abs(ord(item) - ord(stack[-1])) == 32:
                stack.pop(-1)
            else:
                stack.append(item)
        return "".join(stack)

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.makeGood("leEeetcode"))
    print(s.makeGood("abBAcC"))
    print(s.makeGood("s"))
