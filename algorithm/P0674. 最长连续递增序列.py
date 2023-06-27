#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-16 22:24:02
LastEditTime: 2022-01-16 22:39:30
Description:
FilePath: 674.最长连续递增序列.py
"""
#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        increase = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increase[i] = increase[i - 1] + 1
        return max(increase)


# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.findLengthOfLCIS([2, 2, 2, 2, 2]))
