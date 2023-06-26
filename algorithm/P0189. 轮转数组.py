#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-14 23:03:35
LastEditTime: 2022-02-14 23:13:32
Description:
FilePath: 189.轮转数组.py
"""
#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = k % len(nums)
        nums[:] = nums[-r:] + nums[:-r]
        # print(nums)
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    arguments = [1]
    for i, args in enumerate(arguments):
        print("=== *{:02d} INPUT* ===".format(i + 1))
        print(args)
        print("=== *DEBUG* ===")
        solution.rotate([1, 2], 3)
