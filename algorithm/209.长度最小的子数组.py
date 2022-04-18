#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-17 17:40:11
LastEditTime: 2022-04-17 17:44:27
Description: 
FilePath: 209.长度最小的子数组.py
"""
#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
from typing import List
from math import inf


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        left, right, minimum, sum = 0, 0, inf, 0
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                minimum = min(minimum, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        return minimum if minimum != inf else 0


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(ans)
