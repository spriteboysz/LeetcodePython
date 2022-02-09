#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-09 23:50:50
LastEditTime: 2022-02-10 00:05:15
Description: 
FilePath: 150.逆波兰表达式求值.py
'''
#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item in ["+", "-", "*", "/"]:
                a, b = stack.pop(), stack.pop()
                if item == "+":
                    stack.append(b + a)
                if item == "-":
                    stack.append(b - a)
                if item == "*":
                    stack.append(b * a)
                if item == "/":
                    stack.append(int(b / a))
            else:
                stack.append(int(item))
        return stack[-1]
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    # print(s.evalRPN(["2", "1", "+", "3", "*"]))
    # print(s.evalRPN(["4", "13", "5", "/", "+"]))
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11",
          "*", "/", "*", "17", "+", "5", "+"]))
