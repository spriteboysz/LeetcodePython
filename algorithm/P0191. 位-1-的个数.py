#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-08 13:45:49
LastEditTime: 2022-01-08 14:01:02
Description: 位1的个数
FilePath: 191.位-1-的个数.py
"""
#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    n = input()
    print(s.hammingWeight(int(n)))
