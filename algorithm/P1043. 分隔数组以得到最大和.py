#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-18 16:00
FileName: algorithm
Description:P1043. 分隔数组以得到最大和.py 
"""
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            maximum = arr[i - 1]
            for j in range(i - 1, max(-1, i - k - 1), -1):
                dp[i] = max(dp[i], dp[j] + maximum * (i - j))
                if j > 0:
                    maximum = max(maximum, arr[j - 1])
        return dp[len(arr)]


if __name__ == '__main__':
    print(Solution().maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2, 5, 10], k=3))
