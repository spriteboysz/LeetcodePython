#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-08 22:07:43
LastEditTime: 2022-02-08 22:11:09
Description:
FilePath: 2265.根据给定数字划分数组.py
"""
#
# @lc app=leetcode.cn id=2265 lang=python3
#
# [2161] 根据给定数字划分数组
#

# @lc code=start
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lt, eq, gt = [], [], []
        for num in nums:
            if num < pivot:
                lt.append(num)
            elif num > pivot:
                gt.append(num)
            else:
                eq.append(num)
        return lt + eq + gt
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.pivotArray(nums=[9, 12, 5, 10, 14, 3, 10], pivot=10))
    print(s.pivotArray(nums=[-3, 4, 3, 2], pivot=2))
