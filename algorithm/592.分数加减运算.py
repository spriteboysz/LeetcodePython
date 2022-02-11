#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-10 23:45:37
LastEditTime: 2022-02-11 00:11:18
Description: 
FilePath: 592.分数加减运算.py
'''
#
# @lc app=leetcode.cn id=592 lang=python3
#
# [592] 分数加减运算
#

# @lc code=start
from math import gcd
from functools import reduce


class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression.replace("-", "+-").lstrip("+").split("+")
        expression = map(lambda el: list(map(int, el.split("/"))), expression)
        fraction = reduce(lambda a, b: [a[0] * b[1] + b[0]
                                        * a[1], a[1] * b[1]], expression)
        return "/".join(map(lambda el: str(el//gcd(*fraction)), fraction))
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.fractionAddition("-1/2+1/2"))
    print(s.fractionAddition("-1/2+1/2+1/3"))
