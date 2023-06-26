#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-12 23:23:37
LastEditTime: 2022-04-12 23:29:28
Description:
FilePath: 2224.转化时间需要的最少操作数.py
"""
#
# @lc app=leetcode.cn id=2224 lang=python3
#
# [2224] 转化时间需要的最少操作数
#

# @lc code=start
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        hh1, mm1 = map(int, current.split(":"))
        hh2, mm2 = map(int, correct.split(":"))
        minitues = (hh2 - hh1) * 60 + (mm2 - mm1)
        count = 0
        for operator in [60, 15, 5, 1]:
            div, minitues = divmod(minitues, operator)
            count += div
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.convertTime("02:30", "04:35")
    print(ans)
    ans = solution.convertTime("11:00", "11:01")
    print(ans)
