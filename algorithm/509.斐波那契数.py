#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-29 00:01:03
Description: 斐波那契数
FilePath: 509.斐波那契数.py
'''
#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        a, b = 0, 1
        for i in range(2, n + 1):
            c = a + b
            a, b = b, c
        return c


# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.fib(6))
