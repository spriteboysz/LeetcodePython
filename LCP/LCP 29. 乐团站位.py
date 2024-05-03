#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-03 12:32
FileName: LCP
Description:LCP 29. 乐团站位.py 
"""


class Solution:
    def orchestraLayout(self, num: int, x: int, y: int) -> int:
        if x <= y:
            k = min(x, num - 1 - y)
            return (4 * k * (num - k) + 1 + (x + y - k * 2) - 1) % 9 + 1
        kp = min(y, num - 1 - x) + 1
        return (4 * kp * (num - kp) + 1 - (x + y - (kp - 1) * 2) - 1) % 9 + 1


if __name__ == '__main__':
    print(Solution().orchestraLayout(num=4, x=1, y=2))
    print(Solution().orchestraLayout(num=3, x=1, y=1))
