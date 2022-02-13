#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-13 16:38:32
LastEditTime: 2022-02-13 16:54:19
Description: 
FilePath: 128.最长连续序列.py
'''
#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maximum = 0
        for num in nums:
            if num - 1 not in nums:
                cur = num + 1
                while cur in nums:
                    cur += 1
                maximum = max(maximum, cur - num)
        return maximum


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    arguments = [[100, 4, 200, 1, 3, 2], [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]]
    for i, args in enumerate(arguments):
        print("=== {:02d} INPUT ===".format(i + 1))
        print(args)
        print("=== DEBUG ===")
        answer = solution.longestConsecutive(args)
        print("=== OUTPUT ===")
        print(answer)
