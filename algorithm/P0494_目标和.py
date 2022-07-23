#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-03 22:18
LastEditTime: 2022-06-03 22:18
Description:
FilePath: 494.目标和.py
"""
from functools import lru_cache
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache
        def dfs(index, cur):
            if index == -1:
                return cur == 0
            return dfs(index - 1, cur - nums[index]) + dfs(index - 1, cur + nums[index])

        return dfs(len(nums) - 1, target)

if __name__ == '__main__':
    solution = Solution()
    ans = solution.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3)
    print(ans)
