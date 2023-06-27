#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-04 14:13:06
LastEditTime: 2022-02-04 14:14:12
Description:
FilePath: 100322.和为s的两个数字.py
"""
#
# @lc app=leetcode.cn id=100322 lang=python3
#
# [剑指 Offer 57] 和为s的两个数字
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [nums[i], nums[j]]
        return []


if __name__ == '__main__':
    solution = Solution()
    ans = solution.twoSum(nums=[10, 26, 30, 31, 47, 60], target=40)
    print(ans)

# @lc code=end
