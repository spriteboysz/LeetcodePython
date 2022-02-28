#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-28 23:29:21
LastEditTime: 2022-02-28 23:31:08
Description: 
FilePath: 1493.删掉一个元素以后全为-1-的最长子数组.py
"""
#
# @lc app=leetcode.cn id=1493 lang=python3
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#

# @lc code=start
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(0) == 0:
            return len(nums) - 1
        s = "".join(list(map(str, nums))).split("0")
        maximum = 0
        for i in range(len(s) - 1):
            maximum = max(maximum, len(s[i]) + len(s[i + 1]))
        return maximum


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1])
    print(ans)
    ans = solution.longestSubarray([1, 1, 0, 0, 1, 1, 1, 0, 1])
    print(ans)
    ans = solution.longestSubarray([1, 1, 1])
    print(ans)
