#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-05 22:23:55
LastEditTime: 2022-05-19 23:05:04
Description: 
FilePath: 剑指 Offer 45. 把数组排成最小的数.py
"""
#
# @lc app=leetcode.cn id=100323 lang=python3
#
# [剑指 Offer 45] 把数组排成最小的数
#

from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        nums = list(map(str, nums))
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] > nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return "".join(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.minNumber([10, 2]))
    print(s.minNumber([3, 30, 34, 5, 9]))
