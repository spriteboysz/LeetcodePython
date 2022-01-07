#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-05 21:57:15
Description: 
FilePath: 896.单调数列.py
'''
#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        monotonic = sorted(nums)
        if nums == monotonic or nums == monotonic[::-1]:
            return True
        else:
            return False


# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.isMonotonic([1, 2, 2, 3]))
