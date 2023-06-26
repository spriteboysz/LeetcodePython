#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-12 23:58:22
LastEditTime: 2022-02-13 00:10:11
Description:
FilePath: 204.计数质数.py
"""
#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        else:
            prime = [1] * n
            prime[0], prime[1] = 0, 0
            for i in range(2, int(n ** 0.5) + 1):
                if prime[i]:
                    prime[i*i::i] = [0] * len(prime[i*i::i])
            return sum(prime)


# @lc code=end
