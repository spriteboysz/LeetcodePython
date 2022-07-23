#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-11 17:14
LastEditTime: 2022-06-11 17:14
Description:
FilePath: 910.最小差值 II.py
"""

from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        value = nums[-1] - nums[0]
        for i in range(1, len(nums)):
            minimum = min(nums[0] + k, nums[i] - k)
            maximum = max(nums[-1] - k, nums[i - 1] + k)
            value = min(value, maximum - minimum)
        return value


if __name__ == '__main__':
    solution = Solution()
    ans = solution.smallestRangeII(nums=[1, 3, 6], k=3)
    print(ans)
