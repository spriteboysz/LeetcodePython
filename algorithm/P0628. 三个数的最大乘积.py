#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-03 23:53:18
LastEditTime: 2022-02-04 00:00:09
Description: 
FilePath: 628.三个数的最大乘积.py
'''
#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) > 6:
            a, b, c, *nums, d, e, f = sorted(nums)
            nums = [a, b, c, d, e, f]
        product = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    product.append(nums[i] * nums[j] * nums[k])
        return max(product)

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maximumProduct([1, 2, 3]))
    print(s.maximumProduct([1, 2, 3, 4]))
    print(s.maximumProduct([-1, -2, -3]))
