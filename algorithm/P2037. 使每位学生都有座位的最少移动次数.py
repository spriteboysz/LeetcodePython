#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-22 21:36:14
LastEditTime: 2022-01-22 21:41:25
Description:
FilePath: 2037.使每位学生都有座位的最少移动次数.py
"""
#
# @lc app=leetcode.cn id=2037 lang=python3
#
# [2037] 使每位学生都有座位的最少移动次数
#

# @lc code=start
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats, students = sorted(seats), sorted(students)
        count = 0
        for seat, student in zip(seats, students):
            count += abs(seat - student)
        return count
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.minMovesToSeat([2, 2, 6, 6], [1, 3, 2, 6]))
    print(s.minMovesToSeat([4, 1, 5, 9], [1, 3, 2, 6]))
