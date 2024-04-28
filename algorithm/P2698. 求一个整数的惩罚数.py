#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-27 18:13
FileName: algorithm
Description:P2698. 求一个整数的惩罚数.py 
"""


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check(t, x):
            if t == x:
                return True
            d = 10
            while t >= d and t % d <= x:
                if check(t // d, x - (t % d)):
                    return True
                d *= 10
            return False

        return sum([i * i if check(i * i, i) else 0 for i in range(1, n + 1)])


if __name__ == '__main__':
    print(Solution().punishmentNumber(37))
