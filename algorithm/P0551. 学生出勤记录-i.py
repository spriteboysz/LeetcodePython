#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-11 23:24:26
LastEditTime: 2022-01-11 23:26:26
Description:
FilePath: 551.学生出勤记录-i.py
"""
#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start


class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") < 2 and "LLL" not in s:
            return True
        else:
            return False
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.checkRecord("PPALLL"))
