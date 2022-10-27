#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-21 23:01:45
LastEditTime: 2022-04-01 22:16:14
Description: 
FilePath: 15.三数之和.py
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if (c := 0 - (a := nums[i]) - (b := nums[j])) in nums[j + 1:]:
                    result.add(tuple(sorted([a, b, c])))
        return list(map(list, result))


if __name__ == "__main__":
    solution = Solution()
    ans = solution.threeSum([-1, 0, 1, 2, -1, -4])
    print(ans)
    ans = solution.threeSum([0])
    print(ans)
