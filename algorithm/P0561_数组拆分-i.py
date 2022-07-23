#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-13 23:04:45
LastEditTime: 2022-01-13 23:08:12
Description: 数组拆分I
FilePath: 561.数组拆分-i.py
'''
#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分 I
#

# @lc code=start
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.arrayPairSum([6, 2, 6, 5, 1, 2]))
