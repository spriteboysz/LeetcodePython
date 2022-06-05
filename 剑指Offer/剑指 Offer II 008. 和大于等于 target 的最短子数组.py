#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 16:12
LastEditTime: 2022-06-05 16:12
Description:
FilePath: 剑指 Offer II 008. 和大于等于 target 的最短子数组.py
"""

from typing import List
from math import inf

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total, minimum = 0, 0, inf
        for right, num in enumerate(nums):
            total += num
            while total >= target:
                minimum = min(minimum, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if minimum > len(nums) else minimum

if __name__ == '__main__':
    solution = Solution()
    ans = solution.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3])
    print(ans)
