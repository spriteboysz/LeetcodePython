#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-10-04 22:41:04
Description:
FilePath: 1732.找到最高海拔.py
"""
#
# @lc app=leetcode.cn id=1732 lang=python3
#
# [1732] 找到最高海拔
#

# @lc code=start
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        count = len(gain)
        high = [0] * (count + 1)
        for i in range(count):
            high[i + 1] = high[i] + gain[i]

        return max(high)

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.largestAltitude([-5, 1, 5, 0, -7]))
