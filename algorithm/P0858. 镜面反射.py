#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-13 23:09
FileName: algorithm/P0858. 镜面反射.py
Description: 
"""
import math


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        k = p // math.gcd(p, q)
        return 2 if k % 2 == 0 else (k * q // p) % 2


if __name__ == '__main__':
    print(Solution().mirrorReflection(3, 1))
