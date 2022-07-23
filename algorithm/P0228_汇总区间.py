#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-26 23:12:07
Description: 汇总区间
FilePath: 228.汇总区间.py
'''
#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        diff = [-1] * len(nums)
        for i in range(len(nums) - 1):
            diff[i] = nums[i + 1] - nums[i]
        ran = []
        start, end = "", ""
        for i in range(len(nums)):
            if diff[i] != 1 and diff[i - 1] != 1:
                ran.append(str(nums[i]))
            else:
                if i == 0 or diff[i - 1] != 1:
                    start = str(nums[i])
                elif i == len(nums) - 1 or (diff[i - 1] == 1 and diff[i] != 1):
                    end = str(nums[i])
                    ran.append(start + "->" + end)
                    start, end = "", ""

        return ran

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
