#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-10 14:57:34
LastEditTime: 2022-04-10 15:00:54
Description: 
FilePath: 198.打家劫舍.py
"""
#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for k in range(2, len(nums)):
            dp[k] = max(dp[k - 1], nums[k] + dp[k - 2])
        return dp[-1]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.rob([2, 7, 9, 3, 1])
    print(ans)
