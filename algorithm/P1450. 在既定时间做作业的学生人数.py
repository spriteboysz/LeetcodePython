#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-30 23:15:36
LastEditTime: 2022-01-30 23:21:05
Description: 
FilePath: 1450.在既定时间做作业的学生人数.py
'''
#
# @lc app=leetcode.cn id=1450 lang=python3
#
# [1450] 在既定时间做作业的学生人数
#

# @lc code=start
from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        time = [0] * 1001
        for start, end in zip(startTime, endTime):
            for i in range(start, end + 1):
                time[i] += 1
        return time[queryTime]
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.busyStudent([4], [4], 4))
    print(s.busyStudent([4], [4], 5))
    print(s.busyStudent([1, 1, 1, 1], [1, 3, 2, 4], 7))
    print(s.busyStudent([9, 8, 7, 6, 5, 4, 3, 2, 1],
          [10, 10, 10, 10, 10, 10, 10, 10, 10], 5))
