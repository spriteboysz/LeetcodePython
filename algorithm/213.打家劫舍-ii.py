#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-10 15:18:40
LastEditTime: 2022-04-10 15:22:06
Description: 
FilePath: 213.打家劫舍-ii.py
"""
#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def robI(nums: List[int]) -> int:
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            dp = [0] * len(nums)
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for k in range(2, len(nums)):
                dp[k] = max(dp[k - 1], nums[k] + dp[k - 2])
            return dp[-1]

        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]

        return max(robI(nums[0 : n - 1]), robI(nums[1:n]))


# @lc code=end
