#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-28 23:22:17
LastEditTime: 2022-01-28 23:32:44
Description:
FilePath: 1360.日期之间隔几天.py
"""
#
# @lc app=leetcode.cn id=1360 lang=python3
#
# [1360] 日期之间隔几天
#

# @lc code=start


class Solution:
    def calcDays(self, date):
        def isLeap(year):
            return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False

        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = map(int, date.strip().split("-"))
        days = day
        days += sum(months[:month]) + int(isLeap(year) and month >= 3)
        for i in range(1970, year):
            days += 365 + int(isLeap(i))
        return days

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs(self.calcDays(date1) - self.calcDays(date2))
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.daysBetweenDates("2020-01-15", "2019-12-31"))
