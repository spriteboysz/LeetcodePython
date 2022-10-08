#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-23 23:37:10
LastEditTime: 2022-02-23 23:40:11
Description: 
FilePath: 1262.可被三整除的最大和.py
"""
#
# @lc app=leetcode.cn id=1262 lang=python3
#
# [1262] 可被三整除的最大和
#

# @lc code=start
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        if total % 3 == 0:
            return total
        else:
            return total - min(filter(lambda el: el % 3 == total % 3, nums))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.maxSumDivThree([1, 2, 3, 4, 4])
    print(ans)
