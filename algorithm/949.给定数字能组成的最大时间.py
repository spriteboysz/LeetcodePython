#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-15 23:18:54
LastEditTime: 2022-03-15 23:24:05
Description: 
FilePath: 949.给定数字能组成的最大时间.py
"""
#
# @lc app=leetcode.cn id=949 lang=python3
#
# [949] 给定数字能组成的最大时间
#

# @lc code=start
from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort()
        for minitue in range(24 * 60 - 1, -1, -1):
            hour, minitue = divmod(minitue, 60)
            hh, mm = "%02d" % hour, "%02d" % minitue
            num = [int(item) for item in hh + mm]
            if sorted(num) == arr:
                return hh + ":" + mm
        return ""


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.largestTimeFromDigits([1, 2, 3, 4])
    print(ans)
    ans = solution.largestTimeFromDigits([5, 5, 5, 5])
    print(ans)
    ans = solution.largestTimeFromDigits([0, 0, 0, 0])
    print(ans)
    ans = solution.largestTimeFromDigits([0, 0, 1, 0])
    print(ans)
