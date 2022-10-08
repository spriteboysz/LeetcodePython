#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-12 23:21:14
LastEditTime: 2022-02-13 15:58:51
Description: 
FilePath: 227.基本计算器-ii.py
'''
#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        num, stack, operator = 0, [], "+"
        for i, item in enumerate(s):
            if item.isdigit():
                num = num * 10 + int(item)
            if item in "+-*/" or i == len(s) - 1:
                if operator == "+":
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num, operator = 0, item
        return sum(stack)

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    # print(s.calculate("3+2*2"))
    # print(s.calculate(" 3/2 "))
    # print(s.calculate(" 3+5 / 2 "))
    print(s.calculate("14-3/2"))
