#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-12 23:11:34
LastEditTime: 2022-03-12 23:11:58
Description: 
FilePath: 729.我的日程安排表-i.py
"""


#
# @lc app=leetcode.cn id=729 lang=python3
#
# [729] 我的日程安排表 I
#

# @lc code=start
class MyCalendar:
    def __init__(self):
        self.calendars = []

    def book(self, start: int, end: int) -> bool:
        for i, calendar in enumerate(self.calendars):
            if end <= calendar[0]:
                self.calendars.insert(i, (start, end))
                break
            elif end > calendar[0] and start < calendar[1]:
                return False
        else:
            self.calendars.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end
