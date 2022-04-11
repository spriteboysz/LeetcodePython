#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-10 21:45:08
LastEditTime: 2022-04-10 21:47:47
Description: 
FilePath: 53.最大子数组和.py
"""
#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(dp[i - 1] + nums[i], nums[i]))
        print(dp)
        return max(dp)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(ans)
    ans = solution.maxSubArray(nums=[5, 4, -1, 7, 8])
    print(ans)
    ans = solution.maxSubArray([-5, -4, -3, -2, -1])
    print(ans)
