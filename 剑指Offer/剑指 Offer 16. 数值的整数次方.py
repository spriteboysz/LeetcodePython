#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-05 23:00:38
LastEditTime: 2022-02-05 23:08:07
Description:
FilePath: 100295.数值的整数次方.py
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            x, n = 1 / x, -n
        power = 1
        while n:
            if n & 1:
                power *= x
            x *= x
            n //= 2
        return power

if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.0, 10))
    print(s.myPow(2.1, 3))
    print(s.myPow(2.0, -2))
