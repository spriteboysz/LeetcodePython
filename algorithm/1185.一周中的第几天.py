#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-04 15:26:17
Description: 一周中的第几天
FilePath: 1185.一周中的第几天.py
'''
#
# @lc app=leetcode.cn id=1185 lang=python3
#
# [1185] 一周中的第几天
#


# @lc code=start
import time


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        s = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
        return time.strftime("%A", s)

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    s.dayOfTheWeek(4, 10, 2021)
