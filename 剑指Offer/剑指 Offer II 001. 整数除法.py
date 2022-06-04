#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 15:43
LastEditTime: 2022-06-04 15:43
Description:
FilePath: 剑指 Offer II 001. 整数除法.py
"""

class Solution:
    def divide(self, a: int, b: int) -> int:
        flag = False if (a > 0 and b > 0) or (a < 0 and b < 0) else True
        a, b, ret = abs(a), abs(b), 0

        def calc(x, y):
            n = 1
            while x > y << 1:
                y <<= 1
                n <<= 1
            return n, y

        while a >= b:
            cnt, val = calc(a, b)
            ret += cnt
            a -= val
        ret = -ret if flag else ret
        return ret - 1 if ret >= 2 ** 31 else ret

if __name__ == '__main__':
    solution = Solution()
    ans = solution.divide(a=15, b=2)
    print(ans)
