#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-10 23:38:01
LastEditTime: 2022-03-10 23:42:02
Description: 
FilePath: 462.最少移动次数使数组元素相等-ii.py
"""
#
# @lc app=leetcode.cn id=462 lang=python3
#
# [462] 最少移动次数使数组元素相等 II
#

# @lc code=start
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) // 2):
            count += abs(nums[i] - nums[len(nums) - 1 - i])
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minMoves2([1, 2, 3])
    print(ans)
