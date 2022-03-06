#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-06 11:14:01
LastEditTime: 2022-03-06 11:17:40
Description: 
FilePath: 324.摆动排序-ii.py
"""
#
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#

# @lc code=start
from typing import List
from math import ceil


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums.sort()
        mid = ceil(len(nums) / 2)
        nums[::2], nums[1::2] = nums[:mid][::-1], nums[mid:][::-1]
        # print(nums)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.wiggleSort([1, 5, 1, 1, 6, 4])
    print(ans)
    ans = solution.wiggleSort([1, 3, 2, 2, 3])
    print(ans)
    ans = solution.wiggleSort([4, 5, 5, 6])
    print(ans)
