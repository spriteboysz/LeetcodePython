#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-22 22:32:24
LastEditTime: 2022-01-22 22:39:01
Description:
FilePath: 1991.找到数组的中间位置.py
"""
#
# @lc app=leetcode.cn id=1991 lang=python3
#
# [1991] 找到数组的中间位置
#

# @lc code=start
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.findMiddleIndex([1, -1, 4]))
    print(s.findMiddleIndex([2, 5]))
    print(s.findMiddleIndex([1]))
