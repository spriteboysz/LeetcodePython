#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-04 15:12:59
LastEditTime: 2022-02-04 15:13:55
Description:
FilePath: 1000032.消失的数字.py
"""
#
# @lc app=leetcode.cn id=1000032 lang=python3
#
# [面试题 17.04] 消失的数字
#

# @lc code=start
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
