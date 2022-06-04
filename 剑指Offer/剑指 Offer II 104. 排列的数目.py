#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 21:48
LastEditTime: 2022-06-04 21:48
Description:
FilePath: 剑指 Offer II 104. 排列的数目.py
"""

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for t in range(1, target + 1):
            for num in nums:
                if num <= t:
                    dp[t] += dp[t - num]
        return dp[target]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.combinationSum4(nums=[1, 2, 3], target=4)
    print(ans)
