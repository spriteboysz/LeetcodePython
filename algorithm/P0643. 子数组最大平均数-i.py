#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 00:01:56
LastEditTime: 2022-02-04 00:15:32
Description:
FilePath: 643.子数组最大平均数-i.py
'''
#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum, current = sum(nums[:k]), sum(nums[:k])
        for i in range(k, len(nums)):
            current += nums[i] - nums[i - k]
            maximum = max(maximum, current)
        return maximum / k


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.findMaxAverage([5], 1))
