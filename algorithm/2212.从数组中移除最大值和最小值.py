#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-08 22:39:04
LastEditTime: 2022-02-08 22:43:22
Description: 
FilePath: 2212.从数组中移除最大值和最小值.py
'''
#
# @lc app=leetcode.cn id=2212 lang=python3
#
# [2091] 从数组中移除最大值和最小值
#

# @lc code=start
from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        maxindex, minindex = nums.index(max(nums)), nums.index(min(nums))
        a, b = sorted([maxindex, minindex])
        return min(b + 1, n - a, a + 1 + n - b)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.minimumDeletions([0, -4, 19, 1, 8, -2, -3, 5]))
    print(s.minimumDeletions([101]))
