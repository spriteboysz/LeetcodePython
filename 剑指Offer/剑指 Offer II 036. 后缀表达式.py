#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-16 23:56:55
LastEditTime: 2022-05-16 23:56:56
Description: 
FilePath: 剑指 Offer II 036. 后缀表达式.py
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item.isdigit() or item[0] == "-" and item[1:].isdigit():
                stack.append(int(item))
            else:
                print(stack)
                a, b = stack.pop(), stack.pop()
                if item == "+":
                    stack.append(a + b)
                elif item == "-":
                    stack.append(b - a)
                elif item == "*":
                    stack.append(a * b)
                elif item == "/":
                    stack.append(int(b / a))
        return stack[0]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.evalRPN(tokens=["2", "1", "+", "3", "*"])
    print(ans)
    ans = solution.evalRPN(
        tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
    print(ans)
