#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-01 21:42
FileName: algorithm
Description:P2970. 统计移除递增子数组的数目 I.py 
"""
from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def check(nums, left, right) -> bool:
            if left >= 0 and right <= n - 1 and nums[left] >= nums[right]:
                return False
            for i in range(left, 0, -1):
                if nums[i] <= nums[i - 1]:
                    return False
            for i in range(n - 1, right, -1):
                if nums[i] <= nums[i - 1]:
                    return False
            return True

        cnt, n = 0, len(nums)
        for i in range(n):
            for j in range(i, n):
                if check(nums, i - 1, j + 1):
                    cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().incremovableSubarrayCount(nums=[1, 2, 3, 4]))
