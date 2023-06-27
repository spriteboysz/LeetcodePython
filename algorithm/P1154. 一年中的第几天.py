#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-10-04 15:00:33
Description: 一年中的第几天
FilePath: 1154.一年中的第几天.py
"""


#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#

# @lc code=start
class Solution:
    def isLeapYear(self, year: int) -> bool:
        if year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False

    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split("-"))
        mm = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear(year):
            mm[2] = 29

        count = 0
        for i in range(1, month):
            count += mm[i]

        return count + day


# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.dayOfYear("2100-03-01"))
