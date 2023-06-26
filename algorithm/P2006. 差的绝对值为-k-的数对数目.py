#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-22 22:17:41
LastEditTime: 2022-01-22 22:19:54
Description:
FilePath: 2006.差的绝对值为-k-的数对数目.py
"""
#
# @lc app=leetcode.cn id=2006 lang=python3
#
# [2006] 差的绝对值为 K 的数对数目
#

# @lc code=start
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.countKDifference([3, 2, 1, 5, 4], 2))
