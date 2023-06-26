#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-27 23:29:36
LastEditTime: 2022-01-27 23:35:34
Description:
FilePath: 1413.逐步求和得到正数的最小值.py
"""
#
# @lc app=leetcode.cn id=1413 lang=python3
#
# [1413] 逐步求和得到正数的最小值
#

# @lc code=start
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minimum, cur = nums[0], 0
        for num in nums:
            cur += num
            if cur < minimum:
                minimum = cur
        return max(1, 1 - minimum)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.minStartValue([1, 2]))
