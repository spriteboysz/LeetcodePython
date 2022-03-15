#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-14 22:33:38
LastEditTime: 2022-03-14 22:35:49
Description: 
FilePath: 396.旋转函数.py
"""
#
# @lc app=leetcode.cn id=396 lang=python3
#
# [396] 旋转函数
#

# @lc code=start
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total, n = sum(nums), len(nums)
        value = sum([i * v for i, v in enumerate(nums)])
        values = [value]
        for i in range(n - 1):
            value += n * nums[i] - total
            values.append(value)
        return max(values)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.maxRotateFunction([4, 3, 2, 6])
    print(ans)
