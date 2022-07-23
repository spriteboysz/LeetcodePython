#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-06 11:33:27
LastEditTime: 2022-03-06 11:40:48
Description: 
FilePath: 456.132-模式.py
"""
#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132 模式
#

# @lc code=start
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        a = nums[0]
        for j in range(1, len(nums) - 1):
            a, b = min(a, nums[j - 1]), nums[j]
            if a < b:
                for k in range(len(nums) - 1, j, -1):
                    if a < nums[k] < b:
                        return True
        return False


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.find132pattern([1, 2, 3, 4])
    print(ans)
    ans = solution.find132pattern([3, 1, 4, 2])
    print(ans)
    ans = solution.find132pattern([-1, 3, 2, 0])
    print(ans)
