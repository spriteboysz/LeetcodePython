#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-25 22:45:01
LastEditTime: 2022-04-25 22:48:36
Description: 
FilePath: 1800.最大升序子数组和.py
"""
#
# @lc app=leetcode.cn id=1800 lang=python3
#
# [1800] 最大升序子数组和
#

# @lc code=start
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maximum, cur = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                cur += nums[i]
                maximum = max(maximum, cur)
            else:
                cur = nums[i]

        return maximum


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.maxAscendingSum([10, 20, 30, 5, 10, 50])
    print(ans)
