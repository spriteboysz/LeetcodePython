#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-25 22:16:46
LastEditTime: 2022-02-25 22:21:56
Description:
FilePath: 921.使括号有效的最少添加.py
"""


#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#

# @lc code=start


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for item in s:
            if len(stack) == 0 or item == "(":
                stack.append(item)
            if stack[-1] == "(" and item == ")":
                stack.pop()
            else:
                stack.append(item)
        return len(stack)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minAddToMakeValid("()")
    print(ans)
