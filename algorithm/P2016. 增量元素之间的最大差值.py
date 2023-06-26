#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-22 22:05:51
LastEditTime: 2022-01-22 22:13:27
Description:
FilePath: 2016.增量元素之间的最大差值.py
"""
#
# @lc app=leetcode.cn id=2016 lang=python3
#
# [2016] 增量元素之间的最大差值
#

# @lc code=start
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maximum = -1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i] and nums[j] - nums[i] > maximum:
                    maximum = nums[j] - nums[i]
        return maximum
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maximumDifference([9, 4, 3, 2]))
    print(s.maximumDifference([1, 1, 1, 1]))
