#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-22 22:25:18
LastEditTime: 2022-01-22 22:31:23
Description:
FilePath: 1995.统计特殊四元组.py
"""
#
# @lc app=leetcode.cn id=1995 lang=python3
#
# [1995] 统计特殊四元组
#

# @lc code=start
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for a in range(n - 3):
            for b in range(a + 1, n - 2):
                for c in range(b + 1, n - 1):
                    for d in range(c + 1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            count += 1
        return count

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.countQuadruplets([3, 3, 6, 4, 5]))
    print(s.countQuadruplets([1, 1, 1, 3, 5]))
