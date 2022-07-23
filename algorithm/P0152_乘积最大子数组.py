#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-10 22:02:34
LastEditTime: 2022-04-10 22:05:10
Description: 
FilePath: 152.乘积最大子数组.py
"""
#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxRes = curMax = curMin = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                curMax, curMin = curMin, curMax

            curMax = max(curMax * nums[i], nums[i])
            curMin = min(curMin * nums[i], nums[i])
            maxRes = max(maxRes, curMax)

        return maxRes


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.maxProduct([2, 3, -2, 4])
    print(ans)
    ans = solution.maxProduct([-2, 0, -1])
    print(ans)
