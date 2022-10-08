#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-11 17:02
LastEditTime: 2022-06-11 17:02
Description:
FilePath: 713.乘积小于 K 的子数组.py
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count, left, product = 0, 0, 1
        for right, num in enumerate(nums):
            product *= num
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
            count += right - left + 1
        return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100)
    print(ans)
