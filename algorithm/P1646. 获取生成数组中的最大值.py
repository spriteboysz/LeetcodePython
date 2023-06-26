#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-28 23:35:21
LastEditTime: 2022-01-28 23:53:56
Description:
FilePath: 1646.获取生成数组中的最大值.py
"""
#
# @lc app=leetcode.cn id=1646 lang=python3
#
# [1646] 获取生成数组中的最大值
#

# @lc code=start
from math import ceil


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 1:
            return n
        else:
            nums = [0] * (n + 1)
            nums[1] = 1
            for i in range(1, ceil(n / 2)):
                nums[2 * i] = nums[i]
                nums[2 * i + 1] = nums[i] + nums[i + 1]
            return max(nums)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.getMaximumGenerated(2))
