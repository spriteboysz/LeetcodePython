#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 16:21
FileName: LCP
Description:LCR 036. 逆波兰表达式求值.py 
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b, a = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack.pop()


if __name__ == '__main__':
    print(Solution().evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
