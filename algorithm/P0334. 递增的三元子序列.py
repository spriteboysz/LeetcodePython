#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-18 20:14:14
LastEditTime: 2022-03-18 20:15:53
Description: 
FilePath: 334.递增的三元子序列.py
"""
#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

from math import inf
# @lc code=start
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        r1, r2 = inf, inf
        for num in nums:
            if num <= r1:
                r1 = num
            elif num <= r2:
                r2 = num
            else:
                return True
        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.increasingTriplet([1, 2, 3, 4, 5])
    print(ans)
    ans = solution.increasingTriplet([5, 4, 3, 2, 1])
    print(ans)
