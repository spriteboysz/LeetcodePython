#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-05 23:00:38
LastEditTime: 2022-02-05 23:08:07
Description: 
FilePath: 100295.数值的整数次方.py
'''
#
# @lc app=leetcode.cn id=100295 lang=python3
#
# [剑指 Offer 16] 数值的整数次方
#

# @lc code=start


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
        power = 1
        for _ in range(abs(n)):
            power *= x
            if abs(power - power * x) < 0.0000001:
                break
        return power
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.0, 10))
    print(s.myPow(2.1, 3))
    print(s.myPow(2.0, -2))
