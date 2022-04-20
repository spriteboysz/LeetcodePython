#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-20 22:03:02
LastEditTime: 2022-04-20 22:03:57
Description: 
FilePath: 2239.找到最接近-0-的数字.py
"""
#
# @lc app=leetcode.cn id=2239 lang=python3
#
# [2239] 找到最接近 0 的数字
#

# @lc code=start
from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return sorted(nums, key=lambda el: (abs(el), -el))[0]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findClosestNumber([-4, -2, 1, 4, 8])
    print(ans)
    ans = solution.findClosestNumber([-2, -1, 1])
    print(ans)
    ans = solution.findClosestNumber([-10, -100])
    print(ans)
