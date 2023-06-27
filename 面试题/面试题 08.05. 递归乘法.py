#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-07 22:40
LastEditTime: 2022-06-07 22:40
Description: 
FilePath: 面试题 08.05. 递归乘法.py
"""


class Solution:
    def multiply(self, a: int, b: int) -> int:
        a, b = sorted([a, b])
        sum = 0
        for _ in range(a):
            sum += b
        return sum


if __name__ == '__main__':
    solution = Solution()
    ans = solution.multiply(1, 10)
    print(ans)
