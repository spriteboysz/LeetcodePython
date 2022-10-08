#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-13 23:55
LastEditTime: 2022-06-13 23:55
Description:
FilePath: 1014.最佳观光组合.py
"""

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [0] * len(values)
        for i in range(1, len(values)):
            dp[i] = max(dp[i - 1] + values[i] - values[i - 1] -
                        1, values[i] + values[i - 1] - 1)
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.maxScoreSightseeingPair(values=[8, 1, 5, 2, 6])
    print(ans)
    ans = solution.maxScoreSightseeingPair([1, 2])
    print(ans)
