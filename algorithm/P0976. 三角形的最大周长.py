#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-07 22:30:24
LastEditTime: 2022-02-07 22:31:50
Description:
FilePath: 976.三角形的最大周长.py
"""
#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#

# @lc code=start
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.largestPerimeter([1, 2, 1]))
