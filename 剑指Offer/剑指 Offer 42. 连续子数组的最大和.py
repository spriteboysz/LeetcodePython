#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-23 23:30
LastEditTime: 2022-05-23 23:30
Description:
FilePath: 剑指 Offer 42. 连续子数组的最大和.py
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum, cur = nums[0], nums[0]
        for num in nums[1:]:
            cur = max(cur + num, num)
            maximum = max(cur, maximum)
        return maximum


if __name__ == '__main__':
    solution = Solution()
    ans = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(ans)
