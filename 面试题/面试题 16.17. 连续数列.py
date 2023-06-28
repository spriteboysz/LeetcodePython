#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-24 23:06
LastEditTime: 2022-05-24 23:06
Description:
FilePath: 面试题 16.17. 连续数列.py
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        maximum, cur = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur = max(cur + nums[i], nums[i])
            maximum = max(cur, maximum)

        return maximum


if __name__ == '__main__':
    solution = Solution()
    ans = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(ans)
