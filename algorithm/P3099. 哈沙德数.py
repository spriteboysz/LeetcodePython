#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 12:15
FileName: algorithm
Description:P3099. 哈沙德数.py 
"""


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        ss = sum(map(int, list(str(x))))
        if x % ss == 0:
            return ss
        else:
            return -1


if __name__ == '__main__':
    print(Solution().sumOfTheDigitsOfHarshadNumber(18))
