#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-18 23:27:51
LastEditTime: 2022-03-18 23:30:19
Description: 
FilePath: 400.第-n-位数字.py
"""
#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第 N 位数字
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        cur, base = 1, 9
        while n > cur * base:
            n -= cur * base
            cur += 1
            base *= 10
        n -= 1
        num = 10 ** (cur - 1) + n // cur
        index = n % cur
        return num // (10 ** (cur - 1 - index)) % 10


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findNthDigit(11)
    print(ans)
