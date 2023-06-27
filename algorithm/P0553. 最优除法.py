#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-27 22:49:21
LastEditTime: 2022-02-27 23:11:11
Description: 
FilePath: 553.最优除法.py
"""
#
# @lc app=leetcode.cn id=553 lang=python3
#
# [553] 最优除法
#

# @lc code=start
from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) <= 2:
            return "/".join(map(str, nums))
        else:
            return "{}/({})".format(nums[0], "/".join(map(str, nums[1:])))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.optimalDivision([1000, 100, 10, 2])
    print(ans)
    ans = solution.optimalDivision([2])
    print(ans)
