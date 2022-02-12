#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-12 22:08:09
LastEditTime: 2022-02-12 22:15:33
Description: 
FilePath: 75.颜色分类.py
'''
#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for num in nums:
            counts[num] += 1
        nums[:] = sum([[i] * count for i, count in enumerate(counts)], [])
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.sortColors([2, 0, 2, 1, 1, 0]))
    print(s.sortColors([2, 0, 1]))
