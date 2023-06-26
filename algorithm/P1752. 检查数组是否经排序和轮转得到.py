#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-01 22:59:18
LastEditTime: 2022-02-01 23:23:35
Description:
FilePath: 1752.检查数组是否经排序和轮转得到.py
"""
#
# @lc app=leetcode.cn id=1752 lang=python3
#
# [1752] 检查数组是否经排序和轮转得到
#

# @lc code=start
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return nums[i:] + nums[:i] == sorted(nums)
        return True

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.check([2, 1, 3, 4]))
    print(s.check([1, 2, 3]))
    print(s.check([1, 1, 1]))
    print(s.check([2, 1]))
    print(s.check([6, 10, 6]))
