#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 15:48
LastEditTime: 2022-06-04 15:48
Description:
FilePath: 剑指 Offer II 101. 分割等和子集.py
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] | dp[i - num]
        return dp[target]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.canPartition(nums=[1, 5, 11, 5])
    print(ans)
