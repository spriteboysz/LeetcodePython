#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-10-05 22:24:25
Description:
FilePath: 905.按奇偶排序数组.py
"""
#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# @lc code=start
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.sortArrayByParity([3, 1, 2, 4]))
