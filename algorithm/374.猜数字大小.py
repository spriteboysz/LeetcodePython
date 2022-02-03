#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-29 23:53:12
LastEditTime: 2022-02-03 21:45:38
Description: 
FilePath: 374.猜数字大小.py
'''
#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if guess(mid) == -1:
                right = mid
            elif guess(mid) == 1:
                left = mid + 1
            else:
                return mid
        return left


# @lc code=end
