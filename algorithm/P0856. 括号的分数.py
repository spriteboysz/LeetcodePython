#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-13 22:58:52
LastEditTime: 2022-03-13 23:11:38
Description: 
FilePath: 856.括号的分数.py
"""


#
# @lc app=leetcode.cn id=856 lang=python3
#
# [856] 括号的分数
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        point, flag, stack = 0, True, []
        for item in s:
            if item == "(":
                stack.append(item)
                flag = True
            elif item == ")":
                stack.pop()
                if flag:
                    point += 2 ** len(stack)
                    flag = False
        return point


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.scoreOfParentheses("()")
    print(ans)
    ans = solution.scoreOfParentheses("(())")
    print(ans)
    ans = solution.scoreOfParentheses("(()(()))")
    print(ans)
