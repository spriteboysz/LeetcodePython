#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-05 14:06:52
Description: 转变日期格式
FilePath: 1507.转变日期格式.py
'''
#
# @lc app=leetcode.cn id=1507 lang=python3
#
# [1507] 转变日期格式
#

# @lc code=start


class Solution:
    def reformatDate(self, date: str) -> str:
        mon = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        day, month, year = date.split()
        return ("%s-%02d-%02d" %
                (year, int(mon.index(month) + 1), int(day[0:-2])))

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.reformatDate("6th Oct 1933"))
