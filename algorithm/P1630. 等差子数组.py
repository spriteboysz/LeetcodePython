#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-16 23:23:46
LastEditTime: 2022-02-16 23:28:17
Description: 
FilePath: 1630.等差子数组.py
"""
#
# @lc app=leetcode.cn id=1630 lang=python3
#
# [1630] 等差子数组
#

# @lc code=start
from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], left: List[int], right: List[int]) -> List[bool]:
        answer = []
        for start, end in zip(left, right):
            cur = sorted(nums[start: end + 1])
            for i in range(2, len(cur)):
                if cur[i] - cur[i - 1] != cur[i - 1] - cur[i - 2]:
                    answer.append(False)
                    break
            else:
                answer.append(True)
        return answer

# @lc code=end
