#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-11 23:25
LastEditTime: 2022-06-11 23:25
Description:
FilePath: 416. 分割等和子集.py
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        if max(nums) > target:
            return False

        dp = [True] + [False] * target
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.canPartition(nums=[1, 5, 11, 5])
    print(ans)
    ans = solution.canPartition(nums=[1, 2, 3, 5])
    print(ans)
