#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-22 17:05
LastEditTime: 2022-05-22 17:05
Description:
FilePath: 面试题 16.26. 计算器.py.py
"""


class Solution:
    def calculate(self, s: str) -> int:
        factor = s.replace(" ", "").replace("-", "+-").split("+")
        print(factor)
        stack = []



if __name__ == '__main__':
    solution = Solution()
    ans = solution.calculate("3+2*2")
    print(ans)
