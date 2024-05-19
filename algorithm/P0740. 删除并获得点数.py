#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-19 10:52
FileName: algorithm
Description:P0740. 删除并获得点数.py 
"""
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = [0] * 10010
        for num in nums:
            counts[num] += 1
        maximum = max(nums)

        dp = [[0] * 2 for _ in range(maximum + 1)]
        for i in range(1, maximum + 1):
            dp[i][1] = dp[i - 1][0] + i * counts[i]
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
        return max(dp[maximum][0], dp[maximum][1])


if __name__ == '__main__':
    print(Solution().deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]))
