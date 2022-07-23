#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-28 22:22
LastEditTime: 2022-05-28 22:22
Description:
FilePath: 377.组合总和Ⅳ.py
"""
from functools import lru_cache
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(target):
            if target <= 0:
                return target == 0
            return sum(dfs(target - num) for num in nums)

        return dfs(target)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.combinationSum4([1, 2, 3], 4)
    print(ans)
    ans = solution.combinationSum4([9], 3)
    print(ans)
