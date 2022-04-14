#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-14 22:43:05
LastEditTime: 2022-04-14 22:46:18
Description: 
FilePath: 6038.向表达式添加括号后的最小结果.py
"""
#
# @lc app=leetcode.cn id=6038 lang=python3
#
# [6038] 向表达式添加括号后的最小结果
#

# @lc code=start
from math import inf


class Solution:
    def minimizeResult(self, expression: str) -> str:
        num1, num2 = expression.split("+")
        result = []
        for j in range(1, len(num2) + 1):
            for i in range(len(num1)):
                a, b, c, d = (
                    int(num1[:i]) if num1[:i] else 1,
                    int(num1[i:]),
                    int(num2[:j]),
                    int(num2[j:]) if num2[j:] else 1,
                )
                result.append([i, j, a * (b + c) * d])
        i, j, _ = min(result, key=lambda el: el[2])
        return num1[:i] + "(" + num1[i:] + "+" + num2[:j] + ")" + num2[j:]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minimizeResult("12+34")
    print(ans)
    ans = solution.minimizeResult("999+999")
    print(ans)
