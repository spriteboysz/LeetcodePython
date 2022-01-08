#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-08 13:27:56
LastEditTime: 2022-01-08 13:41:30
Description: 
FilePath: 70.爬楼梯.py
'''
#
# @lc app=leetcode.cn id=70 lang=python3
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        else:
            a, b = 1, 2
            for _ in range(3, n + 1):
                a, b = b, a + b
            return b
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(30))
