#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-26 15:22:40
LastEditTime: 2022-02-26 15:25:04
Description: 
FilePath: 32.最长有效括号.py
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maximum = 0
        for i, item in enumerate(s):
            if item == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maximum = max(maximum, i - stack[-1])
        return maximum


if __name__ == "__main__":
    solution = Solution()
    ans = solution.longestValidParentheses("(()")
    print(ans)
    ans = solution.longestValidParentheses(")()())")
    print(ans)
    ans = solution.longestValidParentheses("")
    print(ans)
    ans = solution.longestValidParentheses("()(()")
    print(ans)
