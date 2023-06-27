#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-16 22:05:27
LastEditTime: 2022-03-16 22:06:38
Description: 
FilePath: 1954.收集足够苹果的最小花园周长.py
"""


#
# @lc app=leetcode.cn id=1954 lang=python3
#
# [1954] 收集足够苹果的最小花园周长
#

# @lc code=start
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        i, total = 0, 0
        while total < neededApples:
            i += 2
            total += i * i * 3
        return i * 4

# @lc code=end
