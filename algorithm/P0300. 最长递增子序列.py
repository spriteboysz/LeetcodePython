#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-19 23:42:27
LastEditTime: 2022-04-19 23:42:49
Description: 
FilePath: 300.最长递增子序列.py
"""
#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.lengthOfLIS([10,9,2,5,3,7,101,18])
    print(ans)
