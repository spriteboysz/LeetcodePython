#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 16:27
LastEditTime: 2022-06-05 16:27
Description:
FilePath: 剑指 Offer II 009. 乘积小于 K 的子数组.py
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, product, count = 0, 1, 0
        for right, num in enumerate(nums):
            product *= num
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
            if left <= right:
                count += right - left + 1
        return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100)
    print(ans)
