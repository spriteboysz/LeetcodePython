#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-13 22:05:06
LastEditTime: 2022-04-13 22:07:15
Description: 
FilePath: 2211.统计道路上的碰撞次数.py
"""


#
# @lc app=leetcode.cn id=2211 lang=python3
#
# [2211] 统计道路上的碰撞次数
#

# @lc code=start
class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip("L").rstrip("R")
        return len(directions) - directions.count("S")


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.countCollisions("RLRSLL")
    print(ans)
