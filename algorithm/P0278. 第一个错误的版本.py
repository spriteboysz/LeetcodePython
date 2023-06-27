#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-07 22:26:11
LastEditTime: 2022-02-03 21:56:01
Description:
FilePath: 278.第一个错误的版本.py
"""


class Solution:
    def isBadVersion(self, num):
        return num > 5

    def firstBadVersion(self, n):
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return right
