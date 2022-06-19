#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-19 11:22
LastEditTime: 2022-06-19 11:22
Description:
FilePath: 剑指 Offer 20. 表示数值的字符串.py
"""

from re import match


class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(match(
                '^\\s*[+-]?(\\d+|\\d+\\.|\\d+\\.\\d+|\\.\\d+)([eE][+-]?\\d+)?\\s*$',
                s))


if __name__ == '__main__':
    solution = Solution()
    ans = solution.isNumber(s="0")
    print(ans)
    ans = solution.isNumber(s="e")
    print(ans)
