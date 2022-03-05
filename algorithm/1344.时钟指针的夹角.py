#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-05 16:37:34
LastEditTime: 2022-03-05 16:41:46
Description: 
FilePath: 1344.时钟指针的夹角.py
"""
#
# @lc app=leetcode.cn id=1344 lang=python3
#
# [1344] 时钟指针的夹角
#

# @lc code=start
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mm = 6 * minutes
        hh = hour * 30 + minutes / 2
        angle = abs(hh - mm)
        return min(angle, 360 - angle)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.angleClock(12, 30)
    print(ans)
    ans = solution.angleClock(3, 30)
    print(ans)
    ans = solution.angleClock(3, 15)
    print(ans)
