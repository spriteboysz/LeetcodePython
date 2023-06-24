#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-24 22:04
FileName: algorithm/P2729. 判断一个数是否迷人.py
Description: 
"""


class Solution:
    def isFascinating(self, n: int) -> bool:
        ss = str(n) + str(n * 2) + str(n * 3)
        if len(ss) != 9:
            return False
        digits = [0] * 10
        for c in ss:
            digits[int(c)] += 1

        for i in range(1, 10):
            if digits[i] != 1:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isFascinating(192))
    print(Solution().isFascinating(100))
