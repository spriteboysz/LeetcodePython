#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-19 17:09
FileName: algorithm
Description:P0486. 预测赢家.py 
"""
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n + 1)]
        for j in range(n):
            for i in range(n - j):
                dp[i][i + j] = max(nums[i] - dp[i + 1][i + j], nums[i + j] - dp[i][i + j - 1])
        return dp[0][-1] >= 0


if __name__ == '__main__':
    print(Solution().predictTheWinner(nums=[1, 5, 233, 7]))
