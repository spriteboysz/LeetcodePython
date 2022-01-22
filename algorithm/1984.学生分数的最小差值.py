#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-22 22:42:37
LastEditTime: 2022-01-22 22:48:47
Description: 
FilePath: 1984.学生分数的最小差值.py
'''
#
# @lc app=leetcode.cn id=1984 lang=python3
#
# [1984] 学生分数的最小差值
#

# @lc code=start
from cmath import inf
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        minimum = inf
        for i in range(0, len(nums) - k + 1):
            if nums[i + k - 1] - nums[i] < minimum:
                minimum = nums[i + k - 1] - nums[i]
        return minimum
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.minimumDifference([9, 4, 1, 7], 2))
