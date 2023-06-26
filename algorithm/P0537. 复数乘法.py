#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-07 22:26:11
LastEditTime: 2022-01-11 23:39:33
Description:
FilePath: 537.复数乘法.py
"""
#
# @lc app=leetcode.cn id=537 lang=python3
#
# [537] 复数乘法
#

# @lc code=start


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = map(int, num1.rstrip("i").split("+"))
        c, d = map(int, num2.rstrip("i").split("+"))
        real = str(a * c - b * d)
        imaginary = str(a * d + b * c)
        return real + "+" + imaginary + "i"

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.complexNumberMultiply("1+-1i", "1+-1i"))
