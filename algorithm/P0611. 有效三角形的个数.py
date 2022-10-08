#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-03 22:42
LastEditTime: 2022-06-03 22:42
Description:
FilePath: 611.有效三角形的个数.py
"""

from bisect import bisect_left
from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                index = bisect_left(nums, nums[i] + nums[j])
                if index > j:
                    count += index - 1 - j
        return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.triangleNumber(nums=[2, 2, 3, 4])
    print(ans)
