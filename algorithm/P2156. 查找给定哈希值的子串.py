#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-12 15:59:02
LastEditTime: 2022-02-12 16:10:07
Description:
FilePath: 2156.查找给定哈希值的子串.py
"""
#
# @lc app=leetcode.cn id=2156 lang=python3
#
# [2156] 查找给定哈希值的子串
#

# @lc code=start
from string import ascii_lowercase


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        for i in range(len(s) - k + 1):
            cur = 0
            for j in range(k):
                cur += (ascii_lowercase.index(s[i:i+k][j]) + 1) * power ** j
            if cur % modulo == hashValue:
                return s[i:i+k]
        return -1
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.subStrHash(s="leetcode", power=7, modulo=20, k=2, hashValue=0))
    print(s.subStrHash(s="fbxzaad", power=31, modulo=100, k=3, hashValue=32))
