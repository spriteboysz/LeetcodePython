#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-30 22:14:21
LastEditTime: 2022-01-30 22:18:29
Description:
FilePath: 1827.最少操作使数组递增.py
"""
#
# @lc app=leetcode.cn id=1827 lang=python3
#
# [1827] 最少操作使数组递增
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                count += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return count
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.minOperations([1, 5, 2, 4, 1]))
    print(s.minOperations([8]))
