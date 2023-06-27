#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-05 22:37:16
LastEditTime: 2022-02-05 22:49:51
Description:
FilePath: 100320.数组中数字出现的次数.py
"""
#
# @lc app=leetcode.cn id=100320 lang=python3
#
# [剑指 Offer 56 - I] 数组中数字出现的次数
#

# @lc code=start
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        single = list(set(nums))
        for _ in range(len(nums) - 1, -1, -1):
            num = nums.pop()
            if num in nums:
                single.remove(num)
        return single
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumbers([4, 1, 4, 6]))
    print(s.singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]))
