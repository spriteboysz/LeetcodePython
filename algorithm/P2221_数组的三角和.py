#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-13 21:51:18
LastEditTime: 2022-04-13 21:54:42
Description: 
FilePath: 2221.数组的三角和.py
"""
#
# @lc app=leetcode.cn id=2221 lang=python3
#
# [2221] 数组的三角和
#

# @lc code=start
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            for i in range(len(nums) - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            nums.pop()
        return nums[0]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.triangularSum([1, 2, 3, 4, 5])
    print(ans)
