#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-21 00:01:29
LastEditTime: 2022-01-21 00:23:48
Description:
FilePath: 1021.删除最外层的括号.py
"""
#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        primitive = ""
        start, count = 0, 0
        for i, item in enumerate(s):
            if item == "(":
                count += 1
            elif item == ")":
                count -= 1
            if count == 0:
                primitive += s[start + 1:i]
                start = i + 1      
        return primitive


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    print(s.removeOuterParentheses("(()())(())(()(()))"))
    print(s.removeOuterParentheses("()()"))
