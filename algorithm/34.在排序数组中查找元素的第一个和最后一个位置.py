#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-25 22:24:44
LastEditTime: 2022-02-25 22:29:14
Description: 
FilePath: 34.在排序数组中查找元素的第一个和最后一个位置.py
"""
#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        for i, num in enumerate(nums):
            if num == target and start == -1:
                start = i
            if start != -1 and end == -1 and num > target:
                end = i - 1
            elif start != -1 and end == -1 and i == len(nums) - 1:
                end = i
                break
        return [start, end]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.searchRange([5, 7, 7, 8, 8, 10], 8)
    print(ans)
    ans2 = solution.searchRange([5, 7, 7, 8, 8, 10], 6)
    print(ans2)
    ans3 = solution.searchRange([5, 5, 5], 5)
    print(ans3)
