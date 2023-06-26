#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-28 23:07:46
LastEditTime: 2022-01-28 23:10:36
Description:
FilePath: 724.寻找数组的中心下标.py
"""
#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.pivotIndex([2, 1, -1]))
    print(s.pivotIndex([2, 1, 3]))
