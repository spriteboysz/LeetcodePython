#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-29 22:57:31
LastEditTime: 2022-04-29 22:58:51
Description: 
FilePath: 1414.和为-k-的最少斐波那契数字数目.py
"""
#
# @lc app=leetcode.cn id=1414 lang=python3
#
# [1414] 和为 K 的最少斐波那契数字数目
#

# @lc code=start
from functools import lru_cache


class Solution:
    @lru_cache()
    def findMinFibonacciNumbers(self, k: int) -> int:
        if not k:
            return 0
        a, b = 1, 1
        while b <= k:
            a, b = b, a + b
        return self.findMinFibonacciNumbers(k - a) + 1


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findMinFibonacciNumbers(10)
    print(ans)
