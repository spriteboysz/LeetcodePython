#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-02 23:47:31
LastEditTime: 2022-02-03 00:03:33
Description:
FilePath: 762.二进制表示中质数个计算置位.py
"""
#
# @lc app=leetcode.cn id=762 lang=python3
#
# [762] 二进制表示中质数个计算置位
#

# @lc code=start


class Solution:
    def isPrime(self, num):
        prime = [2, 3, 5, 7, 11, 13, 17, 19]
        if num in prime:
            return True
        elif num == 1:
            return False
        i = 0
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        prime.append(i)
        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            if self.isPrime(bin(i).count("1")):
                count += 1
        return count
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.countPrimeSetBits(6, 10))
    print(s.countPrimeSetBits(10, 15))
