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
        t0, t1, t2 = 0, float('-inf'), float('-inf')  # 已遍历的除以3余数为0、1、2的最大和
        for num in nums:
            idx = num % 3
            if idx == 0:
                t0, t1, t2 = t0 + num, t1 + num, t2 + num
            elif idx == 1:
                t0, t1, t2 = max(t0, t2 + num), max(t1, t0 + num), max(t2, t1 + num)
            elif idx == 2:
                t0, t1, t2 = max(t0, t1 + num), max(t1, t2 + num), max(t2, t0 + num)
        return t0


if __name__ == "__main__":
    solution = Solution()
    ans = solution.maxSumDivThree([1, 2, 3, 4, 4])
    print(ans)
