#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-21 22:02:45
LastEditTime: 2022-01-21 22:03:41
Description: 
FilePath: 2119.反转两次的数字.py
'''
#
# @lc app=leetcode.cn id=2119 lang=python3
#
# [2119] 反转两次的数字
#

# @lc code=start


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        else:
            return bool(num % 10)
# @lc code=end
