#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-21 23:55:09
LastEditTime: 2022-02-22 00:03:45
Description: 
FilePath: 401.二进制手表.py
"""
#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        time = []
        for hour in range(12):
            for minitue in range(60):
                if bin(hour).count("1") + bin(minitue).count("1") == turnedOn:
                    time.append("%d:%02d" % (hour, minitue))
        return time


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.readBinaryWatch(1)
    print(ans)
    ans2 = solution.readBinaryWatch(9)
    print(ans2)
