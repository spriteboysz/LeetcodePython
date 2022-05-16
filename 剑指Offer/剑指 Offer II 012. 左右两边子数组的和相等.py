#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-15 17:43:19
LastEditTime: 2022-05-15 17:43:19
Description: 
FilePath: 剑指 Offer II 012. 左右两边子数组的和相等.py
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, sum_ = 0, sum(nums)
        for i, num in enumerate(nums):
            if left == sum_ - num - left:
                return i
            left += num
        return -1


if __name__ == "__main__":
    solution = Solution()
    ans = solution.pivotIndex([1, 7, 3, 6, 5, 6])
    print(ans)
