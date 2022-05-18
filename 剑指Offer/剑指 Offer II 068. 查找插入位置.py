#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-18 23:07:49
LastEditTime: 2022-05-18 23:07:50
Description: 
FilePath: 剑指 Offer II 068. 查找插入位置.py
"""

from typing import List
from bisect import bisect


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return bisect(nums, target)


if __name__ == "__main__":
    solution = Solution()
    ans = solution.searchInsert(nums=[1, 3, 5, 6], target=5)
    print(ans)
