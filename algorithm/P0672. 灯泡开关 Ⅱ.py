#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-19 10:42
FileName: algorithm
Description:P0672. 灯泡开关 Ⅱ.py 
"""


class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n == 1:
            return 2
        elif n == 2:
            return 3 if presses == 1 else 4
        else:
            return 4 if presses == 1 else 7 if presses == 2 else 8


if __name__ == '__main__':
    print(Solution().flipLights(3, 1))
