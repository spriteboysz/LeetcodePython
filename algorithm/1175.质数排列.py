#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-07 22:09:42
LastEditTime: 2022-02-07 22:17:56
Description: 
FilePath: 1175.质数排列.py
'''
#
# @lc app=leetcode.cn id=1175 lang=python3
#
# [1175] 质数排列
#

# @lc code=start


class Solution:
    def isPrime(self, n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factorial(self, n):
        power = 1
        for i in range(1, n + 1):
            power = (power * i) % (10 ** 9 + 7)
        return power

    def numPrimeArrangements(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            count += int(self.isPrime(i))
        return (self.factorial(count) * self.factorial(n - count)) % (10 ** 9 + 7)

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.numPrimeArrangements(5))
    print(s.numPrimeArrangements(100))
