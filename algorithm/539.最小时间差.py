#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-11 22:41:53
LastEditTime: 2022-02-17 22:57:25
Description: 
FilePath: 539.最小时间差.py
"""
#
# @lc app=leetcode.cn id=539 lang=python3
#
# [539] 最小时间差
#

# @lc code=start
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) != len(set(timePoints)):
            return 0
        else:
            time = []
            for timepoint in timePoints:
                hour, minitue = map(int, timepoint.split(":"))
                time.append(hour * 60 + minitue)
            time.sort()
            time += list(map(lambda el: 1440 + el, time))
            minimum = 3000
            for i in range(1, len(time)):
                minimum = min(minimum, abs(time[i] - time[i - 1]))
            return minimum


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.findMinDifference(timePoints=["23:59", "00:00"])
    print(ans)
    ans = solution.findMinDifference(["05:31","22:08","00:35"])
    print(ans)
