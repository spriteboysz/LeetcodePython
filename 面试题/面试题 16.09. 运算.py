#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-20 23:11:17
LastEditTime: 2022-02-20 23:13:07
Description: 
FilePath: 100350.运算.py
"""


#
# @lc app=leetcode.cn id=100350 lang=python3
#
# [面试题 16.09] 运算
#

# @lc code=start
class Operations:
    def __init__(self):
        pass

    def minus(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> int:
        return int(a / b)

# Your Operations object will be instantiated and called as such:
# obj = Operations()
# param_1 = obj.minus(a,b)
# param_2 = obj.multiply(a,b)
# param_3 = obj.divide(a,b)
# @lc code=end
